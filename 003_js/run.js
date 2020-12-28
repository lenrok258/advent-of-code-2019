var fs = require('fs');

function computeRequiredCanvasSize(wireData) {
    let x = 0;
    let y = 0;
    wireData.forEach(action => {
        const actionCode = action.substring(0, 1)
        const actionValue = parseInt(action.substring(1, action.length))

        if (actionCode == 'R') x += actionValue
        else if (actionCode == 'L') x -= actionValue
        else if (actionCode == 'U') y += actionValue
        else if (actionCode == 'D') y -= actionValue
    })

    console.log(x)
    console.log(y)
}

function emptyCanvas(size) {
    var canvas = []
    for (var i = 0; i < size; i++) {
        canvas[i] = [];
        for (var j = 0; j < size; j++) {
            canvas[i][j] = false;
        }
    }
    return canvas;
}

function drawWireOnCanvas(canvas, wireData) {

    let currentX = 500;
    let currentY = 500;
    canvas[currentX][currentY] = true;
    wireData.forEach(wireAction => {

    });

}


var fileContent = fs.readFileSync("input.txt", 'utf8')
var fileLines = fileContent.split('\n')
var inputDataWire1 = fileLines[0].split(',')
var inputDataWire2 = fileLines[1].split(',')

computeRequiredCanvasSize(inputDataWire1);
computeRequiredCanvasSize(inputDataWire2);
