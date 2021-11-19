$(document).ready(function(){
  
  $(".datetimeinput").datepicker({changeYear: true,changeMonth: true, dateFormat: 'yy-mm-dd'});



  consultardatostemp();
  consultardatoshum();


  setInterval(consultardatos, 4000);














});









// Funcion para recuperar la temperatura 

function consultardatostemp() {
    $.ajax({
       url: "/valorestemp",
        type: 'GET',
        dataType: 'json',
       contentType: 'application/json; charset=utf-8',
      destroy: true,
      success: function (data) {
           temp=data.temperatura.toString()
           simbolo="°c"
           tempfinal=temp+simbolo
           console.log(tempfinal)
           $("#temperatura").html(tempfinal);
           $("#ruta").html(data.ruta);
           $("#actuador").html(data.actuador);
           $("#humedad").html(data.humedad);



            console.log(data)
       }

   });
}



function consultardatoshum() {
  $.ajax({
     url: "/valoreshum",
      type: 'GET',
      dataType: 'json',
     contentType: 'application/json; charset=utf-8',
    destroy: true,
    success: function (data) {
         hum=data.humedad.toString()
         simbolo="%"
         humfinal=hum+simbolo
        
         $("#humedad").html(humfinal);
         $("#rutahum").html(data.ruta);
         $("#actuador").html(data.actuador);



          console.log(data)
     }

 });
}












// $(document).ready(function () {
//   consultardatos();


// setInterval(consultardatos, 4000);
// });




// dash js

