var files;

$('input[type=file]').on('change', prepareUpload);

function prepareUpload(event)
{ 
  files = event.target.files;
}


$(function() {
     $('#post_form').submit(uploadFiles);
});

function uploadFiles()
{
    event.preventDefault();
    $('#myModal1').modal('toggle');
    var csrftoken = $.cookie('csrftoken');
    
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var formData = new FormData();
    
    $.each(files, function(key, value)
    {
        formData.append(key, value);
    });
    
    $.ajax({
        url: $(this).attr('action'),
        type: $(this).attr('method'),
        data: formData,
        cache: false,
        processData: false, // Don't process the files
        contentType: false, // Set content type to false as jQuery will tell the server its a query string request
        success: function(data, textStatus, jqXHR)
        {
            if(typeof data.error === 'undefined')
            {
                console.log('File Upload! : ' + data);
            }
            else
            {
                console.log('ERRORS: ' + data.error);
            }
        },
        error: function(jqXHR, textStatus, errorThrown)
        {
            console.log('ERRORS: ' + textStatus);
        }
    });
}