from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import UserProfile, DenoteForm, UserProfile, UserForm
from project.models import Project, Denote, Category, ProjectPicture
from project.forms import ProjectForm
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, Http404
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_text, force_bytes
from .utils import generate_token
from django.views import View
from .models import MyUser
from django.http import JsonResponse


# Create your views here.


def home(request):
    return render(request, 'account/base.html')


def signup(request):
    form = UserProfile()
    if request.method == 'POST':
        form = UserProfile(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('account/active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })
            send_mail(
                'Active your account',
                message,
                'noreply@gmail.com',
                [user.email]
            )
            # login(request, user)
            return redirect('login')

    return render(request, 'account/signup.html', {'form': form})


class ActiveAccountView(View):

    def get(self, request, uidb64, token):
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(MyUser, pk=uid)
        if user and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('login')
        return redirect('home')


message = {}


def get_total_donotations(user):  #
    sum = 0
    for donation in Denote.objects.filter(user=user):
        sum += donation.amount
    return sum


def profile(request):
    user = get_object_or_404(MyUser, pk=request.user.id)
    projects = Project.objects.filter(user=user)
    donations = Denote.objects.filter(user=user)
    category = Category.objects.all()
    projectform = ProjectForm()
    donationform = DenoteForm()
    userform = UserForm()
    projects_nums = projects.count()
    last_project = 'No Projects'
    if projects:
        last_project = projects.order_by('-start_date').first().title  #
    last_donation = '-------'
    if donations.count():
        last_donation = donations.order_by('-created_at').first().created_at  #
    context = {
        'user': user,
        'projects': projects,
        'donations': donations,
        'category': category,
        'projectform': projectform,
        'donationform': donationform,
        'userform': userform,
        'message': message,
        'user_activaties': {  #
            'projects_nums': projects_nums,
            'last_project': last_project,
            'total_donation': get_total_donotations(user),
            'last_donation': last_donation

        },
    }
    # print(context)
    # return HttpResponse("asdasd")
    return render(request, 'account/profile.html', context)


def update_user_information(request):
    global message
    user = get_object_or_404(MyUser, pk=request.user.id)
    if request.method == 'POST':
        form = UserForm(request.POST)
        # remove constrains on username fields
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.phone = form.cleaned_data.get('phone')
            user.date_of_birth = form.cleaned_data.get('date_of_birth')
            user.country = form.cleaned_data.get('country')
            user.fb_account = form.cleaned_data.get('facebook_profile')
            user.save()
            message = {'status': "alert-success", 'message': "Update Successfully"}
        else:
            message = {'status': 'alert-danger', 'message': 'Update Failure'}

    return redirect('profile_page')


def update_user_avatar(request, user_id):
    user = get_object_or_404(MyUser, pk=user_id)
    if request.method == 'POST':
        if request.FILES.get('avatar'):
            user.avatar = request.FILES.get('avatar')
            user.save()
            message = {'status': 1}
            return redirect('profile_page')
        else:
            message = {'status': 0}
            return JsonResponse(message)


def update_project(request, project_id):
    global message
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project.title = form.cleaned_data.get('title')
            project.details = form.cleaned_data.get('details')
            project.total_target = form.cleaned_data.get('total_target')
            project.start_date = form.cleaned_data.get('start_date')
            project.end_date = form.cleaned_data.get('end_date')
            # get category object then update
            project.category = Category.objects.filter(title=form.cleaned_data.get('category')).first()
            # if uplade new image , clear old images
            if request.FILES.getlist('images'):
                ProjectPicture.objects.filter(project=project).delete()
            # store new image
            for image in request.FILES.getlist('images'):
                ProjectPicture.objects.create(project=project, image=image)
            project.save()
            message = {'status': "alert-success", 'message': "Update Successfully"}
        else:
            print("form error")
            message = {'status': 'alert-danger', 'message': 'Update Failure'}

    return redirect('profile_page')


def delete_project(request, project_id):
    global message
    project = Project.objects.filter(pk=project_id)[0]
    if request.method == 'POST':
        donations = Denote.objects.filter(project=project_id)
        total = 0
        for donation in donations:
            total += donation.amount
        if total < (float(project.total_target) * 0.25):
            project.delete()
            message = {'status': "alert-success", 'message': "Delete Successfully"}
        else:
            message = {'status': "alert-danger", 'message': "Cant Delete This project"}

    return redirect('profile_page')


def update_donation(request, donation_id):
    global message
    donation = get_object_or_404(Denote, pk=donation_id)
    if request.method == "POST":
        form = DenoteForm(request.POST)
        if form.is_valid():
            # donation.project = form.cleaned_data.get('project')
            donation.amount = form.cleaned_data.get('amount')
            donation.save()
            message = {'status': "alert-success", 'message': "Update Successfully"}
        else:
            message = {'status': 'alert-danger', 'message': 'Update Failure'}

    return redirect('profile_page')


def delete_donation(request, donation_id):
    global message
    if request.method == "POST":
        Denote.objects.filter(pk=donation_id)[0].delete()
        message = {'status': "alert-success", 'message': "Delete Successfully"}
    return redirect('profile_page')


def delete_account(request):
    if request.method == "POST":
        global message
        user = MyUser.objects.get(pk=request.user.id)
        if not user.check_password(request.POST['password']):
            message = {'status': "alert-danger", 'message': "Cant Delete Account Password Not Correct "}
            return redirect('profile_page')
        else:
            logout(request)  # logout
            user.delete()
    return redirect('home')
