function consultardatos() {
    $.ajax({
       url: "obtener_valores/",
        type: 'GET',
        dataType: 'json',
       contentType: 'application/json; charset=utf-8',
      destroy: true,
      success: function (data) {
            
           $("#temp").html(data.lectura_sensor);

            console.log(data.lectura + 'sensor')
       }
        
   });
}
$(document).ready(function () {
    consultardatos();


  setInterval(consultardatos, 1);
});
