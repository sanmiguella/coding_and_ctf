const getNotes = require("./notes");
const chalk = require("chalk");

const yargs = require("yargs");

yargs.command({
    command: 'add',
    describe: 'Add a new note',

    builder: {
        title: {
            describe: 'Note Title',
            demandOption: true,
            type: 'string'
        },
        
        body: {
            describe: 'Note Body',
            demandOption: true,
            type: 'string'
        }
    },
    
    handler: function(argv) {
        console.log(`Title: ${argv.title}`);
        console.log(`Body: ${argv.body}`);
    }
}).argv;



//console.log(yargs.argv.add);