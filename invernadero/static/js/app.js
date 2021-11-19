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
      success: function (data,data2) {
          
           $("#temperatura").html(data.temperatura);
           $("#ruta").html(data.ruta);
           $("#actuador").html(data.actuador);



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
    success: function (data,data2) {
        
         $("#humedad").html(data.humedad);
         $("#ruta").html(data.ruta);
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

