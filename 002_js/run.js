var fs = require('fs');

var fileContent = fs.readFileSync("input.txt", 'utf8')
var inputData = fileContent.split(',').map(txt => parseInt(txt, 10))


function computeResultFor(inputData, noun, verb) {
    inputData[1] = noun
    inputData[2] = verb

    for (let i = 0; i < inputData.length; i = i + 4) {
        const instr = inputData[i];
        // console.debug(`Index ${i}, instr=${instr}`);

        if (instr == 99) {
            console.log(`Instr 99 at index = ${i}, result = ${inputData[0]}`)
            return inputData[0]
        }
        else if (instr == 1) {

            const a = inputData[inputData[i + 1]]
            const b = inputData[inputData[i + 2]]
            inputData[inputData[i + 3]] = a + b

        } else if (instr == 2) {

            const a = inputData[inputData[i + 1]]
            const b = inputData[inputData[i + 2]]
            inputData[inputData[i + 3]] = a * b

        } else {
            throw Error(`Unknown instruction ${instr} at index = ${i}`);
        }
    }
}

let inputClone = [...inputData];
let result_1 = computeResultFor(inputClone, 12, 2) // Should be 3516593
console.log(result_1)


for (let noun = 0; noun < 99; noun++) {
    for (let verb = 0; verb < 99; verb++) {
        let inputClone = [...inputData];
        let result = computeResultFor(inputClone, noun, verb)
        if (result == 19690720) {
            const answer = 100 * noun + verb;
            console.log(`Noun ${noun}, verb ${verb}, answer ${answer}`)
            throw Error("Result ready exception :p")
        }
    }
}