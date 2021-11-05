
// Funcion para recuperar la temperatura 

function consultardatos() {
    $.ajax({
       url: "/valores",
        type: 'GET',
        dataType: 'json',
       contentType: 'application/json; charset=utf-8',
      destroy: true,
      success: function (data) {
            
           $("#temperatura").html(data.temperatura);
           $("#ruta").html(data.ruta);

            console.log(data)
       }

   });
}
$(document).ready(function () {
  consultardatos();


setInterval(consultardatos, 8000);
});

