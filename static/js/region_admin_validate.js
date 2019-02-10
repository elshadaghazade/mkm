$('document').ready(function(){
    $.ajax({
        url: 'https://grants.edu.az/api/getregions',
        onSuccess: function(res) {
            console.log("AAA", res)
        }
    })

    $('#id_name').on('keyup', function(){
        
    })
})