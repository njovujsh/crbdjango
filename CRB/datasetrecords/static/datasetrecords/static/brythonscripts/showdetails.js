$(document).ready(function()
{
    $('a#showclientdetails').click(function()
    {
        var value = $(this).attr("href");
        request_details(value);
        return false;
    });
    return false;
});

function request_details(details)
{
    $.ajax({
        url:"/data/requestinfo/byid/",
        type: "get",
        data: {"userdetails":details},
        dataType:'json',
        async: 'true',
        
        success: function(data, status, xhr){
            console.log("What is the problem with ajax");
            var returned_data = $(data);
            $("#clientdetailsresponses").clear().append(returned_html);
            $("#myModal").modal("show");
        },
        
        failure: function(info){
            alert("Got some failure");
        }
    });
    
    //alert(details);
}
