const fs = require('fs');
const chalk = require('chalk');
const fileName = 'data.json';

// Read data
var dataBuffer = fs.readFileSync(fileName); // Binary data
var dataJSON = dataBuffer.toString(); // Convert data to string
var data = JSON.parse(dataJSON); // Parse JSON data into an object

// Shows original data
console.log(`${chalk.yellow.bold("Original data")}`);
console.log(`${chalk.red("Name: ")} ${chalk.green(data.name)}`);
console.log(`${chalk.red("Age: ")} ${chalk.green(data.age)}`);

// Change data
data.name = "zabuza"; 
data.age = "35"; 

// Shows modified data
console.log(`${chalk.yellow.bold("\nModified data")}`);
console.log(`${chalk.red("Name: ")} ${chalk.green(data.name)}`);
console.log(`${chalk.red("Age: ")} ${chalk.green(data.age)}`);

// Write data 
dataJSON = JSON.stringify(data); 
fs.writeFileSync(fileName, dataJSON);