var input = {
    key: [],
    mouseButtons: [],
    mousex: 0,
    mousey: 0,
    mousedx: 0,
    mousedy: 0,
    lastmousex: 0,
    lastmousey: 0,
    wheeldx: 0,
    wheeldy: 0,
};

const ButtonState = {
    IDLE: "idle",
    DOWN: "down",
    PRESSED: "pressed",
    UP: "up"
};

var MAX_KEYS = 300;
var MAX_BUTTONS = 10;

function InitInput() {
    for (var i = 0; i < 300; ++i) {
        input.key[i] = ButtonState.IDLE;
    }
    for (var i = 0; i < 10; ++i) {
        input.mouseButtons[i] = ButtonState.IDLE;
    }
    document.onkeydown = handleKeyDown;
    document.onkeyup = handleKeyUp;
    document.onmousedown = handleMouseDown;
    document.onmouseup = handleMouseUp;
    document.onmousemove = handleMouseMove;
    document.onwheel = handleWheelEvent;
}

function processInputEvents() {
    var speed = 1;

    // camera switch
    for (var i = 0; i < cameras.length; ++i)
        if (input.key[i + 97] == ButtonState.DOWN || input.key[i + 49] == ButtonState.DOWN) {
            selectedCamera = i;
        }

    //W
    if (input.key[87] == ButtonState.PRESSED || input.key[87] == ButtonState.DOWN) {
        cameras[selectedCamera].position[2] -= speed * time.deltaSeconds;
    }
    //S
    if (input.key[83] == ButtonState.PRESSED || input.key[83] == ButtonState.DOWN) {
        cameras[selectedCamera].position[2] += speed * time.deltaSeconds;
    }
    //A
    if (input.key[65] == ButtonState.PRESSED || input.key[65] == ButtonState.DOWN) {
        cameras[selectedCamera].position[0] += speed * time.deltaSeconds;
    }
    //D
    if (input.key[68] == ButtonState.PRESSED || input.key[68] == ButtonState.DOWN) {
        cameras[selectedCamera].position[0] -= speed * time.deltaSeconds;
    }

    // R
    if (input.key[82] == ButtonState.DOWN) {
        cameras[selectedCamera].position = [0.0, 0.0, 10.0];
        cameras[selectedCamera].yaw = 0.0;
        cameras[selectedCamera].pitch = 0.0;
    }

    if (input.mouseButtons[0] == ButtonState.PRESSED) {
        var rotation_speed = 0.1;
        cameras[selectedCamera].yaw += input.mousedx * time.deltaSeconds * rotation_speed;
        cameras[selectedCamera].pitch += input.mousedy * time.deltaSeconds * rotation_speed;
    }
    if (input.mouseButtons[1] == ButtonState.DOWN || input.mouseButtons[1] == ButtonState.PRESSED) {
        cameras[selectedCamera].position[0] += input.mousedx * time.deltaSeconds * 0.1;
        cameras[selectedCamera].position[1] -= input.mousedy * time.deltaSeconds * 0.1;
    }
    var speed_zoom = 0.1;
    cameras[selectedCamera].position[2] += input.wheeldy * time.deltaSeconds * speed_zoom;

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
    for (var i = 0; i < MAX_BUTTONS; ++i) {
        if (input.mouseButtons[i] == ButtonState.UP) {
            input.mouseButtons[i] = ButtonState.IDLE;
        } else if (input.mouseButtons[i] == ButtonState.DOWN) {
            input.mouseButtons[i] = ButtonState.PRESSED;
        }
    }
    for (var i = 0; i < MAX_KEYS; ++i) {
        if (input.key[i] == ButtonState.UP) {
            input.key[i] = ButtonState.IDLE;
        }
    }
    input.mousedx = 0;
    input.mousedy = 0;
    input.wheeldy = 0;
}