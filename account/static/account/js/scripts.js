$(function(){

  setTimeout(function() {
    $('#message').fadeOut('slow');
  }, 1000);


  $('#info_link').click()


  $('input').blur(function(){
       element=$(this)

       if(element.attr("name") == "phone")
  {
    console.log("phone validations")
    let regExp=RegExp('^(010|012|011)[0-9]{9}')
      if(!regExp.test($(this).val()))
          ($(this).addClass("is-invalid"))
      else
      ($(this).removeClass("is-invalid"))
  }
    
    if(element.attr("type") == "text")
  {
    console.log("text validations")
      if(!$(this).val())
          ($(this).addClass("is-invalid"))
      else
      ($(this).removeClass("is-invalid"))
  }
  else if(element.attr("type") == "number")
  {
      if($(this).val()<=0)
          ($(this).addClass("is-invalid"))
      else
      ($(this).removeClass("is-invalid"))
  }
  })


  $('select').blur(function(){
    if($(this).val()< 1 )
        ($(this).addClass("is-invalid"))
    else
      ($(this).removeClass("is-invalid"))})

    $('textarea').blur(function(){
    if(!$(this).val())
      ($(this).addClass("is-invalid"))
    else
      ($(this).removeClass("is-invalid"))})


    $('input[type="date"]').change(function(){
         if($(this).attr('name') == 'start_date')
      {
        start_date=new Date($(this).val())
        end_date=new Date($('#id_end_date').val())

        if(start_date > end_date)
          $(this).addClass("is-invalid")
        else
          $(this).removeClass("is-invalid")



      }
      else if($(this).attr('name') == 'end_date')
      {
        end_date=new Date($(this).val())
        start_date=new Date($('#id_start_date').val())

          if(end_date < start_date)
            $(this).addClass("is-invalid")
          else
            $(this).removeClass("is-invalid")
      }
    })


})

function validation(form_id)
{
  vaild=true
  $($('#'+form_id).prop('elements')).each(function(){

    if ($(this).hasClass('is-invalid'))
        vaild=false
})
  if(vaild)
    $("#"+form_id).submit();
}