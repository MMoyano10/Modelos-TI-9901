
/*desarmar el cubo*/
function desarmarCubo() {
    var gridItems = document.getElementsByClassName('grid-item');
    var colores = ['white', 'yellow', 'red', 'orange', 'green', 'blue'];
    
    // Colores de las casillas del medio
    var middleColors = [
      gridItems[4], // Centro
      gridItems[13], // Medio izquierdo
      gridItems[22], // Medio derecho
      gridItems[31], // Medio superior
      gridItems[40], // Medio inferior
      gridItems[49]  // Medio frontal
    ];
    
    // Mantener los colores de las casillas del medio sin cambios
    for (var i = 0; i < middleColors.length; i++) {
      middleColors[i].style.backgroundColor = middleColors[i].style.backgroundColor;
    }
    
    // Asignar colores aleatorios a las demás casillas
    for (var i = 0; i < gridItems.length; i++) {
      if (!middleColors.includes(gridItems[i])) {
        var color = colores[Math.floor(Math.random() * colores.length)];
        gridItems[i].style.backgroundColor = color;
      }
    }
  }

/*Armar cubo */  

// Función para armar el cubo con los colores originales
function armarCubo() {
  var gridItems = document.getElementsByClassName('grid-item');
  
  // Colores para cada casilla del cubo
  var coloresCubo = [
    '#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff'
  ];
  
  // Asignar los colores del cubo a las casillas correspondientes
  for (var i = 0; i < gridItems.length; i++) {
    gridItems[i].style.backgroundColor = coloresCubo[i];
  }
}