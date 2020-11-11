
$("#formulario_contacto").validate({
    rules: {
        nombre:{
            required: true,
            minlenght: 3,
            maxlenght:30
        },
        email:{
            required: true,
            email: true
        },
        tipo_solicitud: {
            required:true
        },
        mensaje: {
            required: true,
            minlenght: 5,
            maxlenght: 200
        }
    }
})



$("#guardar").click(function(){
    if($("#formulario_contacto").valid() == false){
        return;
    }
    let nombre =$("#nombre").val()
    let email =$("#email").val()
    let tipoSolicitud =$("#tipo_solicitud").val()
    let mensaje =$("#mensaje").val()
    let avisos =$("#avisos").is(":checked")
})