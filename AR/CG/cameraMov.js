function processInputEvents() {
    var speed = 10;
    //W
    if (input.key[87] == ButtonState.PRESSED || input.key[87] == ButtonState.DOWN) {
        camera.position[2] -= speed * time.deltaSeconds;
    }
    //S
    if (input.key[83] == ButtonState.PRESSED || input.key[83] == ButtonState.DOWN) {
        camera.position[2] += speed * time.deltaSeconds;
    }
    //A
    if (input.key[65] == ButtonState.PRESSED || input.key[65] == ButtonState.DOWN) {
        camera.position[0] -= speed * time.deltaSeconds;
    }
    //D
    if (input.key[68] == ButtonState.PRESSED || input.key[68] == ButtonState.DOWN) {
        camera.position[0] += speed * time.deltaSeconds;
    }
    if (input.key[82] == ButtonState.DOWN) {
        camera = {
            position: [0.0, 0.0, 10.0],
            yaw: 0.0,
            pitch: 0.0
        };
    }
    if (input.mouseButtons[0] == ButtonState.PRESSED) {
        var rotation_speed = 0.1;
        camera.yaw += input.mousedx * time.deltaSeconds * rotation_speed;
        camera.pitch += input.mousedy * time.deltaSeconds * rotation_speed;
    }
    if (input.mouseButtons[1] == ButtonState.DOWN || input.mouseButtons[1] == ButtonState.PRESSED) {

    }
    var speed_zoom = 0.1;
    camera.position[2] += input.wheeldy * time.deltaSeconds * speed_zoom;
}

function handleWheelEvent(event) {
    input.wheeldx = event.deltaX;
    input.wheeldy = event.deltaY;
}

function handleKeyDown(event) {
    if (input.key[event.keyCode] == ButtonState.DOWN) {
        input.key[event.keyCode] = ButtonState.PRESSED;
    } else {
        input.key[event.keyCode] = ButtonState.DOWN;
    }
}

function handleMouseUp(event) {
    input.mouseButtons[event.button] = ButtonState.UP;
}

function handleMouseMove(event) {
    var mousex = event.clientX;
    var mousey = event.clientY;
    input.mousedx = mousex - input.lastmousex;
    input.mousedy = mousey - input.lastmousey;
    input.lastmousex = mousex;
    input.lastmousey = mousey;
}

function handleKeyUp(event) {
    input.key[event.keyCode] = ButtonState.UP;
}

function handleMouseDown(event) {
    input.mouseButtons[event.button] = ButtonState.DOWN;
    input.lastmousex = event.clientX;
    input.lastmousey = event.clientY;
}

function UpdateInput() {
    for (var i = 0; i < 10; ++i) {
        if (input.mouseButtons[i] == ButtonState.UP) {
            input.mouseButtons[i] = ButtonState.IDLE;
        } else if (input.mouseButtons[i] == ButtonState.DOWN) {
            input.mouseButtons[i] = ButtonState.PRESSED;
        }
    }
    for (var i = 0; i < 300; ++i) {
        if (input.key[i] == ButtonState.UP) {
            input.key[i] = ButtonState.IDLE;
        }
    }
    input.mousedx = 0;
    input.mousedy = 0;
    input.wheeldy = 0;
}