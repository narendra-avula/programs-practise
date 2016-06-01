$(document).ready(function () {
    console.log('Hello narendra');

    $(function(){
        $('.change-div').click(function () {
            id = $(this).attr('id');
        });
    });

    $(function(){
        apiUrl = 'https://hackerearth.0x10.info/api/accolite_product?type=json&query=list_product'
        $.getJSON(apiUrl, function(data) {
            console.log(data);
            $("#count").text(data.menu.length);

            var count = 0;
            for (var i=0; i<data.menu.length; i++){
                if (data.menu[i].name == 'Cyber Security'){
                    console.log(count);
                }
                count++;
            }
            $('#change-image').attr('src',data.menu[count-1].image);
            $("#section-title").text(data.menu[count-1].name);
            $('#link').attr('href',data.menu[count-1].link);
            $("#likes").text(25);
            $("#description").text(data.menu[count-1].description);
        });
    });

});