$(function(){
  $('[data-toggle="tooltip"]').tooltip();
});

function validarRetiro(){
  for (var i = 0; i < document.tipo_despacho.fecha_retiro.length; i++) {
    if (document.tipo_despacho.fecha_retiro[i].checked) {
      document.tipo_despacho.fechatmp.value = document.tipo_despacho.fecha_retiro[i].value;
    }
  }
}

function validarDespacho(){
  for (var i = 0; i < document.tipo_despacho.fecha_despacho.length; i++) {
    if (document.tipo_despacho.fecha_despacho[i].checked) {
      document.tipo_despacho.fechaEntregaTmp.value = document.tipo_despacho.fecha_despacho[i].value;
    }
  }
}

function obtenerFecha(control){
  console.log(control);
  var radios = document.getElementsByName(control);
  var valores;
  for (var i = 0; i < radios.length; i++) {
    if (radios[i].checked){
      valores = radios[i].value.split(";");
    }
  }
  if (Array.isArray(valores)){  
    var fecha_despacho = valores[0];
    var precio_despacho = valores[1];

    fecha_field = document.getElementById('id_fecha_entrega');
    estado_field = document.getElementById('id_estado');

    fecha_field.value = fecha_despacho;
    estado_field.value = "Activo"
  }
}

function validarSucursal(valor){
 //alert(document.tipo_despacho.sucursal.value)
 document.tipo_despacho.sucursaltmp.value = valor;
}

function validarRegion(valor){
 document.tipo_despacho.regiontmp.value = valor;
}

function validarComuna(valor){
 document.tipo_despacho.comunatmp.value = valor;
}

function ocultar(control){
  console.log('im in');
  if(document.getElementById('logo-placeholder').style.display != "none") {
    $("#logo-placeholder").fadeOut(400);
  }
  if(control=='envio'){
    document.getElementById('envio').style.display = "none";
    $("#retiro").fadeIn(600);
  }

  if(control=='retiro'){
    document.getElementById('retiro').style.display = "none";
    $("#envio").fadeIn(600);
  }
}