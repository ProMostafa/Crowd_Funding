$(function(){

  setTimeout(function() {
    $('#message').fadeOut('slow');
  }, 1000);
  $('#info_link').click()

//   $('#avatar-photo').change( function(){
//     console.log('change avatar' );
//     $('#avatar-form').submit();
// });

// get fro user object
//$('#id_country').val('EG')


// update avatar
// $('#avatar-form').submit(function (e) {
//   var data;

//   data = new FormData();
//   data.append('file', $('#avatar-photo')[0].files[0]);
//   console.log('ajax call' );
//   $.ajax({
//       url: `http://127.0.0.1:8000/update_user_avatar/${3}`,
//       data: data,
//       processData: false,
//       type: 'POST',

//       // This will override the content type header, 
//       // regardless of whether content is actually sent.
//       // Defaults to 'application/x-www-form-urlencoded'
//       contentType: 'multipart/form-data', 

//       // //Before 1.5.1 you had to do this:
//       // beforeSend: function (x) {
//       //     if (x && x.overrideMimeType) {
//       //         x.overrideMimeType("multipart/form-data");
//       //     }
//       // },
//       // Now you should be able to do this:
//       mimeType: 'multipart/form-data',    //Property added in 1.5.1

//       success: function (data) {
//           alert(data);
//       }
//   });

//   e.preventDefault();
// });





  $('input').blur(function(){
       element=$(this)

       if(element.attr("name") == "phone")
  {
    console.log("phone validations")
    let regExp=RegExp('^(010|012|011)[0-9]{8}')
      if(!regExp.test($(this).val()))
          ($(this).addClass("is-invalid"))
      else
      ($(this).removeClass("is-invalid"))
  }
   else if(element.attr("type") == "text")
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
  vaild = true
  $($('#'+form_id).prop('elements')).each(function(){

    if ($(this).hasClass('is-invalid'))
        vaild=false
    })
  if(vaild)
    $("#"+form_id).submit();
}
