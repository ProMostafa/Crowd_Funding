$(document).ready(function () {
    $('.toast').not("#report-toast").toast('show');
})
$("#project-report-btn").click(function(){
    $.ajax({
        url: '/project/report/',
        method: 'GET',
        data:{
            body: $("#report-message").val(),
            project: $("#project_id").val()
        },
        success: function(data){
            if (data.return){
                $('#report-toast').toast('show')
                $("#report-message").val('')
                $("#exampleModal").modal("hide")
            }else{
                alert("error reporting")
            }
        }
    })

})

$('#commentReportModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var comment = button.data('comment') // Extract info from data-* attributes
  var modal = $(this)
  modal.find('.created-by').text('created by '+ button.data('created-by'))

  $("#commentReportBtn").click(function(){
    $.ajax({
            url: `/comment_report/${comment}`,
            method: 'GET',
            data:{
                body: $("#commentReportMessage").val()
            },
            success: function(data){
            console.log(data)
                if (data.return){
                    $('#report-toast').toast('show')
                    $("#commentReportMessage").val('')
                    $("#commentReportModal").modal("hide")
                }else{
                    alert("error reporting")
                }
            }
        })
    })
})

 var average_rating;
 var number_of_rating;
 var first_load=true
$(function(){
   
   
    $('#average_rating').click()
    $('#rating_num_value').text(number_of_rating)

    $("[data-rating-stars]").each(function () {
        // Get all data-rating attributes
        let d = {},
            re_dataAttr = /^data-rating\-(.+)$/;

        $.each($(this).get(0).attributes, function (index, attr) {
            if (re_dataAttr.test(attr.nodeName)) {
                let key = attr.nodeName.match(re_dataAttr)[1];
                d[key] = attr.nodeValue;
            }
        });

        // Create the click event handler
        if (d.input != null) {
            d.click = function (e) {
                $(d.input).val(e.stars);
            }
        }

        // Run the rating function on the element
        $(this).rating(d);
    });

   
    
    $("#review").rating({
        "value": average_rating,  // avr_rate  --> project.average_rating
          "click":function (e) {
            let arr= window.location.href.split('/');
            project_id=arr[arr.length-1]
            console.log("start click")
            if(!first_load){
                console.log("Ajax call")
                $.ajax({
                    //url: `/project_rate/${3}>/${e.stars}`,
                    url:`http://127.0.0.1:8000/project_rate/${project_id}/${e.stars}`,
                    dataType: 'json',
                    success: function (data) {
                        console.log("make rating")
                        console.log(data.status); 
                        console.log(data.number_of_rating)
                        $('#rating_num_value').text(data.number_of_rating)
                    }
                  });
            }
            else
                first_load = false
           
          }
        });   
})

function get_average_rating(av_rating,num_rating){
    average_rating= Math.floor( av_rating ); 
    number_of_rating=Math.floor( num_rating ); 
}


const defaults = {
    "value": 0,
    "stars": 5,
    "half": false,
    "emptyStar": "far fa-star",
    "halfStar": "fas fa-star-half-alt",
    "filledStar": "fas fa-star",
    "color": "#fcd703",
    "readonly": false,
    "click": function (e) {
        console.error("No click callback provided!");
    }
};

jQuery.fn.extend({
    rating: function (options = {}) {
        return this.each(function () {
            if ($(this).attr("rating")) {
                $(this).empty();
            }

            this.stars = options.value ? options.value : defaults.value;
            this.readonly = options.readonly ? options.readonly : defaults.readonly;

            this.getStars = function () {
                return $(this).find($("i"));
            };

            $(this).css({
                "color": options.color ? options.color : defaults.color
            })
                .attr("rating", true);

            if (!this.readonly) {
                $(this).off('mousemove').on('mousemove', function (e) {
                    let halfStars = options.half ? options.half : defaults.half;

                    if (this.getStars().index(e.target) >= 0) {
                        if (!halfStars) {
                            $(this).find("i").attr("class", options.emptyStar ? options.emptyStar : defaults.emptyStar);
                            let index = this.getStars().index(e.target) + 1;

                            for (let i = 0; i < this.getStars().length; i++) {
                                if (i < index)
                                    $(this.getStars()[i]).attr("class", options.filledStar ? options.filledStar : defaults.filledStar)
                            }

                        } else {
                            $(this).find("i").attr("class", options.emptyStar ? options.emptyStar : defaults.emptyStar);
                            let extra = 0.5;

                            $(this).find("i").css({
                                "width": $(this).find("i").outerWidth()
                            });

                            if (e.offsetX > ($(e.target).outerWidth() / 2))
                                extra = 1;

                            let index = this.getStars().index(e.target) + extra;
                            for (let i = 0; i < this.getStars().length; i++) {
                                if (i + 0.5 < index) {
                                    $(this.getStars()[i]).attr("class", options.filledStar ? options.filledStar : defaults.filledStar)
                                } else if (i < index) {
                                    $(this.getStars()[i]).attr("class", options.halfStar ? options.halfStar : defaults.halfStar)
                                }
                            }
                        }
                    }
                });

                $(this).off('mouseout').on('mouseout', function (e) {
                    this.printStars();
                });

                $(this).off('click').on('click', function (e) {
                    let halfStars = options.half ? options.half : defaults.half;
                    if (!halfStars) {
                        this.stars = this.getStars().index(e.target) + 1;
                    } else {
                        let extra = 0.5;
                        if (e.offsetX > ($(e.target).outerWidth() / 2))
                            extra = 1;

                        this.stars = this.getStars().index(e.target) + extra;
                    }

                    const callback = options.click ? options.click : defaults.click;
                    callback({
                        "stars": this.stars,
                        "event": e
                    });
                });
            }

            // Add star elements to the element
            const stars = options.stars ? options.stars : defaults.stars;
            for (let i = 0; i < stars; i++) {
                let star = $("<i></i>")
                    .addClass(options.emptyStar ? options.emptyStar : defaults.emptyStar)
                    .appendTo($(this));

                if (!this.readonly) {
                    star.css({
                        "cursor": "pointer",
                        "font-size":" 2.5rem",
                    })
                }

                if (i > 1000)
                    return;
            }

            this.printStars = function () {
                let halfStars = options.half ? options.half : defaults.half;
                if (!halfStars) {
                    $(this).find("i").attr("class", options.emptyStar ? options.emptyStar : defaults.emptyStar);
                    for (let i = 0; i < this.stars; i++) {
                        $(this.getStars()[i]).attr("class", options.filledStar ? options.filledStar : defaults.filledStar)
                    }
                } else {
                    $(this).find("i").attr("class", options.emptyStar ? options.emptyStar : defaults.emptyStar);
                    for (let i = 0; i < this.stars; i++) {
                        if (i < this.stars - 0.5) {
                            $(this.getStars()[i]).attr("class", options.filledStar ? options.filledStar : defaults.filledStar)
                        } else {
                            $(this.getStars()[i]).attr("class", options.halfStar ? options.halfStar : defaults.halfStar)
                        }
                    }
                }
            };

            if (this.stars > 0) {
                this.printStars();

                const callback = options.click ? options.click : defaults.click;
                callback({
                    "stars": this.stars
                });
            }
        });
    }
})

