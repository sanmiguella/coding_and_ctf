const fs = require('fs');
const targetFile = 'notes.json';
const chalk = require('chalk');

const getNotes = function() {
    return "Your notes...";
}

const addNote = function(title, body) {
    const notes = loadNotes();

    const duplicateNotes = notes.filter(function(note) {
        return note.title === title
    });

    console.log(`${chalk.red.bold("Duplicate found: ")} ${duplicateNotes.length}`)

    if (duplicateNotes.length === 0) {
        notes.push({
            title: title,
            body: body
        });

        saveNotes(notes);
        console.log(`\n${chalk.yellow.bold("New note added!")}`);

    } else {
        console.log(`\n${chalk.yellow.bold("Note title taken!")}`);
    }
}

const removeNote = function(title) {
    const notes = loadNotes();

    if (notes.length > 0) {
        const notesToKeep = notes.filter(function(note) {
            return note.title !== title;
        });


        if (notes.length > notesToKeep.length) {
            saveNotes(notesToKeep);
            console.log(`${chalk.yellow.bold(`Removed ${title}!`)}`);
            
        } else {
            console.log(`${chalk.yellow.bold(`${title} not found!`)}`);
        }

    } else {
        console.log(`${chalk.yellow.bold("At least one entry is needed for remove command to be used.")}`);
    }
}

const saveNotes = function(notes) {
    const dataJSON = JSON.stringify(notes);
    fs.writeFileSync(targetFile, dataJSON);
}

const loadNotes = function() {
    try {
        const dataBuffer = fs.readFileSync(targetFile);
        const dataJSON = dataBuffer.toString();

        return JSON.parse(dataJSON);

    } catch(e) {
        return [];
    }
}

module.exports = {
    getNotes: getNotes,
    addNote: addNote,
    removeNote: removeNote
}