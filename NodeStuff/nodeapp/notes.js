const fs = require('fs');
const targetFile = 'notes.json';

const getNotes = function() {
    return "Your notes...";
}

const addNote = function(title, body) {
    const notes = loadNotes();

    const duplicateNotes = notes.filter(function(notes) {
        return notes.title === title
    });

    console.log(`Duplicate found : ${duplicateNotes.length}`)

    if (duplicateNotes.length === 0) {
        notes.push({
            title: title,
            body: body
        });

        saveNotes(notes);
        console.log("\nNew note added!");

    } else {
        console.log("\nNote title taken!");
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
    addNote: addNote
}