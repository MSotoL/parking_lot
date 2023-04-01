// Defino las variables generales

var width = 900;
var height = 500;
var shadowOffset = 20;
var tween = null;

// Espacio en pixels para el "snap" del grid.
var blockSnapSize = 15;

var plazaNum = 0
var carreteraNum = 0
var columnaNum=0

var arrPlazas=[];

// ####################################################
// #####  CREO EL ESCENARIO DONDE VOY A DIBUJAR  ######
// ####################################################
var stage = new Konva.Stage({
  container: 'lienzo',
  width: width,
  height: height
});

// ####################################################
// #########  CREO UN GRID DE REFERENCIA   ############
// ####################################################
var gridLayer = new Konva.Layer();
var padding = blockSnapSize;
console.log(width, padding, width / padding);
for (var i = 0; i < width / padding; i++) {
  gridLayer.add(new Konva.Line({
    points: [Math.round(i * padding) + 0.5, 0, Math.round(i * padding) + 0.5, height],
    stroke: '#ddd',
    strokeWidth: 1,
  }));
}

gridLayer.add(new Konva.Line({points: [0,0,10,10]}));
for (var j = 0; j < height / padding; j++) {
  gridLayer.add(new Konva.Line({
    points: [0, Math.round(j * padding), width, Math.round(j * padding)],
    stroke: '#ddd',
    strokeWidth: 0.5,
  }));
}

// ####################################################
// ######  DEFINICIÓN DE SOMBRAS DE LAS FIGURAS  ######
// ####################################################
var sombraPlazaGr_H = new Konva.Rect({
  x: 0,
  y: 0,
  width: blockSnapSize * 6,
  height: blockSnapSize * 4,
  fill: '#FF7B17',
  opacity: 0.6,
  stroke: '#CF6412',
  strokeWidth: 3,
  dash: [20, 2]
});

var sombraPlazaGr_V = new Konva.Rect({
  x: 0,
  y: 0,
  width: blockSnapSize * 4,
  height: blockSnapSize * 6,
  fill: '#FF7B17',
  opacity: 0.6,
  stroke: '#CF6412',
  strokeWidth: 3,
  dash: [20, 2]
});

var sombraPlazaPq_H = new Konva.Rect({
  x: 0,
  y: 0,
  width: blockSnapSize * 6,
  height: blockSnapSize * 3,
  fill: '#FF7B17',
  opacity: 0.6,
  stroke: '#CF6412',
  strokeWidth: 3,
  dash: [20, 2]
});

var sombraPlazaPq_V = new Konva.Rect({
  x: 0,
  y: 0,
  width: blockSnapSize * 3,
  height: blockSnapSize * 6,
  fill: '#FF7B17',
  opacity: 0.6,
  stroke: '#CF6412',
  strokeWidth: 3,
  dash: [20, 2]
});

var sombraColumna = new Konva.Circle({
  x: 0,
  y: 0,
  width: blockSnapSize * 2,
  height: blockSnapSize * 2,
  fill: '#FF7B17',
  opacity: 0.6,
  stroke: '#CF6412',
  strokeWidth: 3,
  dash: [20, 2]
});

var sombraCarretera_H = new Konva.Rect({
  x: 0,
  y: 0,
  width: blockSnapSize * 15,
  height: blockSnapSize * 4,
  fill: '#FF7B17',
  opacity: 0.6,
  stroke: '#CF6412',
  strokeWidth: 3,
  dash: [20, 2]
});

var sombraCarretera_V = new Konva.Rect({
  x: 0,
  y: 0,
  width: blockSnapSize * 4,
  height: blockSnapSize * 15,
  fill: '#FF7B17',
  opacity: 0.6,
  stroke: '#CF6412',
  strokeWidth: 3,
  dash: [20, 2]
});

// ####################################################
// ########  FUNCIONES DE CREACIÓN DE FIGURAS  ########
// ####################################################

// Plaza grande HORIZONTAL
function nuevaPlazaGr_H(x, y, layer, stage) {
  // Creo un rectángulo de Konva
  let plazaGr_H = new Konva.Rect({
    x: x,
    y: y,
    width: blockSnapSize * 6,
    height: blockSnapSize * 4,
    fill: 'green',
    stroke: '#ddd', // borde
    strokeWidth: 1,
    draggable: true, 
    id:'gr_' + plazaNum //identificador de plaza
  });
  // Evento inicio de "drag" (arrastrar)
  plazaGr_H.on('dragstart', (e) => {
    // Al comenzar a arrastrar una plaza muestro la sombra
    sombraPlazaGr_H.show();
    sombraPlazaGr_H.moveToTop();
    plazaGr_H.moveToTop();
  });
  // Evento fin de "drag" (arrastrar)
  plazaGr_H.on('dragend', (e) => {
    plazaGr_H.position({
      // Recalculo la posición de la plaza para que haga "snap" con el grid
      x: Math.round(plazaGr_H.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(plazaGr_H.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
    // Oculto la sombra
    sombraPlazaGr_H.hide();
  });
  // Evento mientras hacemos un movimiento de "drag" (arrastrar)
  plazaGr_H.on('dragmove', (e) => {
    // Recalculo la posición de la sombra para que haga "snap" con el grid
    sombraPlazaGr_H.position({
      x: Math.round(plazaGr_H.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(plazaGr_H.y() / blockSnapSize) * blockSnapSize
    });
    // Repintamos el área de Stage
    stage.batchDraw();
  });
  // Añado la plaza a la capa
  layer.add(plazaGr_H);
  plazaNum+=1;
  stage.batchDraw()
}

// Plaza grande VERTICAL
function nuevaPlazaGr_V(x, y, layer, stage) {
  let plazaGr_V = new Konva.Rect({
    x: x,
    y: y,
    width: blockSnapSize * 4,
    height: blockSnapSize * 6,
    fill: 'green',
    stroke: '#ddd',
    strokeWidth: 1,
    draggable: true,
    id:'gr_' + plazaNum
  });
  plazaGr_V.on('dragstart', (e) => {
    sombraPlazaGr_V.show();
    sombraPlazaGr_V.moveToTop();
    plazaGr_V.moveToTop();
  });
  plazaGr_V.on('dragend', (e) => {
    plazaGr_V.position({
      x: Math.round(plazaGr_V.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(plazaGr_V.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
    sombraPlazaGr_V.hide();
  });
  plazaGr_V.on('dragmove', (e) => {
    sombraPlazaGr_V.position({
      x: Math.round(plazaGr_V.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(plazaGr_V.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
  });

  layer.add(plazaGr_V);
  plazaNum+=1;
  stage.batchDraw()
}

// Plaza pequeña HORIZONTAL
function nuevaPlazaPq_H(x, y, layer, stage) {
  let plazaPq_H = new Konva.Rect({
    x: x,
    y: y,
    width: blockSnapSize * 6,
    height: blockSnapSize * 3,
    fill: '#00E000',
    stroke: '#ddd',
    strokeWidth: 1,
    draggable: true,
    id:'pq_' + plazaNum
  });
  plazaPq_H.on('dragstart', (e) => {
    sombraPlazaPq_H.show();
    sombraPlazaPq_H.moveToTop();
    plazaPq_H.moveToTop();
  });
  plazaPq_H.on('dragend', (e) => {
    plazaPq_H.position({
      x: Math.round(plazaPq_H.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(plazaPq_H.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
    sombraPlazaPq_H.hide();
  });
  plazaPq_H.on('dragmove', (e) => {
    sombraPlazaPq_H.position({
      x: Math.round(plazaPq_H.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(plazaPq_H.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
  });
  layer.add(plazaPq_H);
  plazaNum+=1;
  stage.batchDraw()
}

// Plaza pequeña VERTICAL
function nuevaPlazaPq_V(x, y, layer, stage) {
  let plazaPq_V = new Konva.Rect({
    x: x,
    y: y,
    width: blockSnapSize * 3,
    height: blockSnapSize * 6,
    fill: '#00E000',
    stroke: '#ddd',
    strokeWidth: 1,
    draggable: true,
    id:'pq_' + plazaNum
  });
  plazaPq_V.on('dragstart', (e) => {
    sombraPlazaPq_V.show();
    sombraPlazaPq_V.moveToTop();
    plazaPq_V.moveToTop();
  });
  plazaPq_V.on('dragend', (e) => {
    plazaPq_V.position({
      x: Math.round(plazaPq_V.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(plazaPq_V.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
    sombraPlazaPq_V.hide();
  });
  plazaPq_V.on('dragmove', (e) => {
    sombraPlazaPq_V.position({
      x: Math.round(plazaPq_V.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(plazaPq_V.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
  });
  layer.add(plazaPq_V);
  plazaNum+=1;
  stage.batchDraw()
}

// Plaza discapacitados HORIZONTAL
function nuevaPlazaDc_H(x, y, layer, stage) {
  // Creo un rectángulo de Konva
  let plazaDc_H = new Konva.Rect({
    x: x,
    y: y,
    width: blockSnapSize * 6,
    height: blockSnapSize * 4,
    fill: 'blue',
    stroke: '#ddd', // borde
    strokeWidth: 1,
    id:'dc_' + plazaNum //identificador de plaza
  });
  plazaDc_H.on('dragstart', (e) => {
    sombraPlazaGr_H.show();
    sombraPlazaGr_H.moveToTop();
    plazaDc_H.moveToTop();
  });
  plazaDc_H.on('dragend', (e) => {
    plazaDc_H.position({
      x: Math.round(plazaDc_H.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(plazaDc_H.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
    sombraPlazaGr_H.hide();
  });
  plazaDc_H.on('dragmove', (e) => {
    sombraPlazaGr_H.position({
      x: Math.round(plazaDc_H.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(plazaDc_H.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
  });
  layer.add(plazaDc_H);
  plazaNum+=1;
  stage.batchDraw()
}

// Plaza discapacitados VERTICAL
function nuevaPlazaDc_V(x, y, layer, stage) {
  let plazaDc_V = new Konva.Rect({
    x: x,
    y: y,
    width: blockSnapSize * 4,
    height: blockSnapSize * 6,
    fill: 'blue',
    stroke: '#ddd',
    strokeWidth: 1,
    draggable: true,
    id:'dc_' + plazaNum
  });
  plazaDc_V.on('dragstart', (e) => {
    sombraPlazaGr_V.show();
    sombraPlazaGr_V.moveToTop();
    plazaDc_V.moveToTop();
  });
  plazaDc_V.on('dragend', (e) => {
    plazaDc_V.position({
      x: Math.round(plazaDc_V.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(plazaDc_V.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
    sombraPlazaGr_V.hide();
  });
  plazaDc_V.on('dragmove', (e) => {
    sombraPlazaGr_V.position({
      x: Math.round(plazaDc_V.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(plazaDc_V.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
  });
  layer.add(plazaDc_V);
  plazaNum+=1;
  stage.batchDraw()
}

// Columna
function nuevaColumna(x, y, layer, stage) {
  // Creo un círculo de Konva
  let columna = new Konva.Circle({
      x: x,
      y: y,
      width: blockSnapSize * 2,
      height: blockSnapSize * 2,
      fill: 'red',
      stroke: '#ddd',
      strokeWidth: 1,
      shadowColor: 'black',
      shadowBlur: 2,
      shadowOffset: {x : 1, y : 1},
      shadowOpacity: 0.4,
      draggable: true,
      id:'co_' + columnaNum
  });
  columna.on('dragstart', (e) => {
      sombraColumna.show();      
      sombraColumna.moveToTop();
      columna.moveToTop();
  });
  columna.on('dragend', (e) => {
    columna.position({
          x: Math.round(sombraColumna.x() / blockSnapSize) * blockSnapSize,
          y: Math.round(sombraColumna.y() / blockSnapSize) * blockSnapSize
      });
      stage.batchDraw();
      sombraColumna.hide();
  });
  columna.on('dragmove', (e) => {
    sombraColumna.position({
          x: Math.round(columna.x() / blockSnapSize) * blockSnapSize,
          y: Math.round(columna.y() / blockSnapSize) * blockSnapSize
      });
      stage.batchDraw();
  });
  layer.add(columna);
  columnaNum+=1;
  stage.batchDraw()
}

// Carretera HORIZONTAL
function nuevaCarretera_H(x, y, layer, stage) {
  let carret_H = new Konva.Rect({
    x: x,
    y: y,
    width: blockSnapSize * 15,
    height: blockSnapSize * 4,
    fill: 'grey',
    draggable: true,
    id:'cr_' + carreteraNum
  });
  carret_H.on('dragstart', (e) => {
    sombraCarretera_H.show();
    sombraCarretera_H.moveToTop();
    carret_H.moveToTop();
  });
  carret_H.on('dragend', (e) => {
    carret_H.position({
      x: Math.round(carret_H.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(carret_H.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
    sombraCarretera_H.hide();
  });
  carret_H.on('dragmove', (e) => {
    sombraCarretera_H.position({
      x: Math.round(carret_H.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(carret_H.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
  });
  layer.add(carret_H);
  carreteraNum+=1;
  stage.batchDraw()
}

// Carretera VERTICAL
function nuevaCarretera_V(x, y, layer, stage) {
  let carret_V = new Konva.Rect({
    x: x,
    y: y,
    width: blockSnapSize * 4,
    height: blockSnapSize * 15,
    fill: 'grey',   
    draggable: true,
    id:'cr_' + carreteraNum
  });
  carret_V.on('dragstart', (e) => {
    sombraCarretera_V.show();
    sombraCarretera_V.moveToTop();
    carret_V.moveToTop();
  });
  carret_V.on('dragend', (e) => {
    carret_V.position({
      x: Math.round(carret_V.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(carret_V.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
    sombraCarretera_V.hide();
  });
  carret_V.on('dragmove', (e) => {
    sombraCarretera_V.position({
      x: Math.round(carret_V.x() / blockSnapSize) * blockSnapSize,
      y: Math.round(carret_V.y() / blockSnapSize) * blockSnapSize
    });
    stage.batchDraw();
  });
  layer.add(carret_V);
  carreteraNum+=1;
  stage.batchDraw()
}

function nPlazaGr_H() {   
  nuevaPlazaGr_H(blockSnapSize * 20, blockSnapSize * 10, layer, stage);    
};
function nPlazaGr_V() {   
  nuevaPlazaGr_V(blockSnapSize * 20, blockSnapSize * 10, layer, stage);    
};

function nPlazaPq_H() {   
  nuevaPlazaPq_H(blockSnapSize * 20, blockSnapSize * 10, layer, stage);    
};
function nPlazaPq_V() {   
  nuevaPlazaPq_V(blockSnapSize * 20, blockSnapSize * 10, layer, stage);    
};

function nPlazaDc_H() {   
  nuevaPlazaDc_H(blockSnapSize * 20, blockSnapSize * 10, layer, stage);    
};

function nPlazaDc_V() {   
  nuevaPlazaDc_V(blockSnapSize * 20, blockSnapSize * 10, layer, stage);    
};

function nColumna() {   
  nuevaColumna(blockSnapSize * 20, blockSnapSize * 10, layer, stage);    
};

function nCarr_H() {   
  nuevaCarretera_H(blockSnapSize * 20, blockSnapSize * 10, layer, stage);    
};

function nCarr_V() {   
  nuevaCarretera_V(blockSnapSize * 20, blockSnapSize * 10, layer, stage);    
};

function borrar() {   
  window.location.reload();
};

// ####################################################
// ########  CREO LA CAPA DONDE VOY A DIBUJAR  ########
// ####################################################
var layer = new Konva.Layer();

sombraPlazaGr_H.hide();
layer.add(sombraPlazaGr_H);
sombraPlazaGr_V.hide();
layer.add(sombraPlazaGr_V);
sombraPlazaPq_H.hide();
layer.add(sombraPlazaPq_H);
sombraPlazaPq_V.hide();
layer.add(sombraPlazaPq_V);
sombraColumna.hide();
layer.add(sombraColumna);
sombraCarretera_H.hide();
layer.add(sombraCarretera_H);
sombraCarretera_V.hide();
layer.add(sombraCarretera_V);

// ####################################################
// #####  AÑADO AL ESCENARIO EL GRID Y LA CAPA  #######
// ####################################################
stage.add(gridLayer);
stage.add(layer);

// ####################################################
// #####        GUARDAR IMAGEN DEL DIBUJO       #######
// ####################################################

function downloadURI(uri, name) {
  var link = document.createElement('a');
  link.download = name;
  link.href = uri;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  delete link;
}

function guardarImagen(){

  document.getElementById('btnGuardar').addEventListener(
    'click',
    function () {
      var dataURL = stage.toDataURL({ pixelRatio: 3 });
      downloadURI(dataURL, 'stage.png');
    },
    false
  );

}

// ####################################################
// #####      MOSTRAR/CERRAR DIV DE AYUDA       #######
// ####################################################
function ayuda(){
  document.getElementById('ayuda').style.visibility='initial';
}

function cerrarAyuda(){
  document.getElementById('ayuda').style.visibility='hidden';
}

// ####################################################
// #####        GUARDAR DATOS DE LA PLAZA       #######
// ####################################################
function guardarInfoPlaza(){

  var objPlaza = {
    id: 0,
    descripcion: "",
    observaciones: "",
    planta: 0,
    tipo : 0,
  }
  
  objPlaza.descripcion=document.getElementById('plzDescrip').value;
  objPlaza.observaciones=document.getElementById('plzObserv').value;

  var URLactual = window.location.href;
  var plantaURL=URLactual.slice(URLactual.lastIndexOf('/')+1, URLactual.length);  
  objPlaza.planta=Number(plantaURL);
  
  switch(document.getElementById('plzTipoPlaza').value){
    case 'Grande':
      objPlaza.tipo=1;
      break;
    case 'Pequeña':
      objPlaza.tipo=2;
      break;
    case 'Discapacitados':
      objPlaza.tipo=3;
      break;
  }

  // ENVIAR LOS DATOS AL SERVIDOR MEDIANTE AJAX
  // Creo un JSON con el objeto plaza
  const plazaJSON = JSON.stringify(objPlaza);

  // Envío el JSON al servidor con AJAX
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    // Aquí controlo la respuesta del servidor
    const respuesta=JSON.parse(this.responseText)
    if (respuesta.resultado=="OK"){
      alert("La plaza se ha insertado correctamente.");
    }
    else{
      alert("Ha ocurrido un error al insertar la plaza.");
    }
  }

  //Llamo a la vista guardar_plaza_BD
  xhttp.open("POST", "/guardar_plaza_BD");
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("plaza=" + plazaJSON + "&csrfmiddlewaretoken="+document.getElementsByName('csrfmiddlewaretoken')[0].value);

  objPlaza.id=respuesta.id;
  arrPlazas.push(objPlaza);

  document.getElementById('frmPlaza').style.visibility='hidden';

}


// ####################################################
// #####  CREO EL MENÚ CONTEXTUAL DE CADA FORMA  ######
// ####################################################
let currentShape;
var menuNode = document.getElementById('menu');
document.getElementById('btnInformacion').addEventListener('click', () => {
  var strFig = currentShape.attrs.id;
  var strFigura = "";  
  if (strFig.slice(0, 2)=="co" || strFig.slice(0, 2)=="cr") {
    alert("Ha pulsado sobre una figura que no es una Plaza.\nNo se puede añadir información de esta figura (columnas o carreteras).");
  }
  else{
    document.getElementById('plzID').value=strFig.slice(3, strFig.length);
    document.getElementById('plzID').disabled=true;
    if (strFig.slice(0, 2)=="gr") {
      strFigura="Grande";
    }
    else if (strFig.slice(0, 2)=="pq") {
      strFigura="Pequeña";
    }
    else {
      strFigura="Discapacitados";
    }
    document.getElementById('plzDescrip').value="";
    document.getElementById('plzObserv').value="";    
    document.getElementById('plzTipoPlaza').value=strFigura;
    document.getElementById('plzTipoPlaza').disabled=true;
    document.getElementById('frmPlaza').style.visibility='initial';
  }
});

document.getElementById('btnBorrarFig').addEventListener('click', () => {
  // Borrar figura
  currentShape.destroy();  
});

window.addEventListener('click', () => {
  // Oculto el menu contextual
  menuNode.style.display = 'none';
});

stage.on('contextmenu', function (e) {
  // Elimino el menú contextual por defecto
  e.evt.preventDefault();
  if (e.target === stage) {
    // Si la llamada es sobre el escenario no hago nada
    return;
  }
  // en caso contrario... muestro el menú contextual que he generado
  currentShape = e.target;
  menuNode.style.display = 'initial';
  var containerRect = stage.container().getBoundingClientRect();
  menuNode.style.top =
    containerRect.top + stage.getPointerPosition().y + 4 + 'px';
  menuNode.style.left =
    containerRect.left + stage.getPointerPosition().x + 4 + 'px';
});

function cerrarFormulario(){
  document.getElementById('frmPlaza').style.visibility='hidden';
}