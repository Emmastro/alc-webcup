$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")
    create_post();
});


function create_post() {
    console.log("create post is working!")
    console.log($('#post-text').val())
};

function create_post() {
    console.log("create post is working!")
    $.ajax({
        url : "create_post/",
        type : "POST",
        data : { the_post : $('#post-text').val() },

        success : function(json) {
            $('#post-text').val('');
            console.log(json);
            console.log("success");
        },

        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>");
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
};