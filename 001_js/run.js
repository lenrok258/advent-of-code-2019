var fs = require('fs');


function compute_fuel(mass) {
    var fuel = Math.floor(mass / 3) - 2
    if (fuel < 0) {
        return 0;
    } 

    return fuel + compute_fuel(fuel);

}

var file = fs.readFileSync("input.txt", 'utf8')
var inputData = file.split("\n")

var fuelTotal = inputData
    .map(compute_fuel)
    .reduce((prv, curr) => prv + curr)

console.log(fuelTotal)
