function descargar_archivo(data, nombre_archivo) {
    var archivo_final, linkExportar;

    archivo_final = new Blob(
            [data], 
            {type: "text/csv"}
        );

    //Insertamos un link en el documento
    linkExportar = document.createElement("a");
    linkExportar.download = nombre_archivo;
    linkExportar.href = window.URL.createObjectURL(archivo_final);
    //pero oculto
    linkExportar.style.display = "none";
    //inserción
    document.body.appendChild(linkExportar);
    //apertura
    linkExportar.click();
}

function exportar_tabla(nombre_archivo) {
    var datos = [];
    var filas = document.querySelectorAll("table tr");
    
    for (var i = 0; i < filas.length; i++) {
        var row = [], cols = filas[i].querySelectorAll("td, th");
        
        for (var j = 0; j < cols.length; j++) 
            row.push(cols[j].innerText);
        
        datos.push(row.join(","));        
    }

    descargar_archivo(datos.join("\n"), nombre_archivo);
}