// Code starts
// you must use this function and may not edit it

function output(msg) {
    console.log(this.type, ":", msg)
}

function warning(type) {
    this.type = type;
    this.output = output;
}

var errorMsg = new warning("error");
var warningMsg = new warning("warning");

// Do not edit below this line.

errorMsg.output('You have been disconnected!');
warningMsg.output('You have been idle for 15 minutes');
