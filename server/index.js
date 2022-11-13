const WebSocket = require("ws");

const wss = new WebSocket.Server({port:8082});

wss.on("connection", ws=> {
    console.log("New client connected");
    ws.send("hello budy!")
    ws.on("message", message => {
        console.log(`Received message: ${message}`)
    })

    ws.on("close", () => {
        console.log("Client has disconnected");
    });
});
