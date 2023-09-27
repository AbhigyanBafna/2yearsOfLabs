const fs = require('fs');
const path = require('path');

function createFile(filename, content) {
    const writeStream = fs.createWriteStream(filename);
    writeStream.write(content, 'utf8');
    writeStream.end(() => {
        console.log(`${filename} created.`);
    });
}

function readFile(filename) {
    const readStream = fs.createReadStream(filename, 'utf8');
    let content = '';
    readStream.on('data', chunk => {
        content += chunk;
    });

    readStream.on('end', () => {
        console.log(`Reading ${filename}...`);
        console.log(content);
    });
}

function appendToFile(filename, content) {
    const writeStream = fs.createWriteStream(filename, { flags: 'a' });
    writeStream.write(content, 'utf8');
    writeStream.end(() => {
        console.log(`Appended to ${filename}.`);
    });
}

function renameFile(oldFilename, newFilename) {
    fs.rename(oldFilename, newFilename, err => {
        if (err) throw err;
        console.log(`${oldFilename} renamed to ${newFilename}.`);
    });
}

function deleteFile(filename) {
    fs.unlink(filename, err => {
        if (err) throw err;
        console.log(`${filename} deleted.`);
    });
}

const demoFile = 'demo.txt';
const renamedFile = 'file_to_delete.txt';

createFile(demoFile, 'Hello, world!');
readFile(demoFile);
appendToFile(demoFile, '\nThis is an appended line.');
renameFile(demoFile, renamedFile);
deleteFile(renamedFile);
