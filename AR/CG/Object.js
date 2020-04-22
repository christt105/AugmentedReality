class Object {
    constructor(name) {
        this.name = name;

        this.x = 0.0;
        this.y = 0.0;

        this.rot = 0.0;
        this.axis_rot = [0.0, 0.0, 1.0];

        this.mirror_h = false;
        this.mirror_v = false;
    }

    createBuffers() {
        this.createVertexBuffer(this.vertices, this.colors);
        this.createIndexBuffer(this.indices);
    }

    createVertexBuffer(vertices, colors) {
        this.id_v = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, this.id_v);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);

        this.id_c = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, this.id_c);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(colors), gl.STATIC_DRAW);
    }

    createIndexBuffer(indices) {
        this.id_i = gl.createBuffer();
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.id_i);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(indices), gl.STATIC_DRAW)
    }

    setPosition(x, y) {
        this.x = x;
        this.y = y;
    }

    setRotation(rot, axis = [0.0, 0.0, 1.0]) {
        this.rot = rot;
        this.axis_rot = axis;
    }

    setMirrorH(value) {
        this.mirror_h = value;
    }

    setMirrorV(value) {
        this.mirror_v = value;
    }

    draw() {
        gl.bindBuffer(gl.ARRAY_BUFFER, this.id_v);
        gl.vertexAttribPointer(shaderProgram.vertexPositionAttribute, 3, gl.FLOAT, false, 0, 0);

        gl.bindBuffer(gl.ARRAY_BUFFER, this.id_c);
        gl.vertexAttribPointer(shaderProgram.vertexColorAttribute, 3, gl.FLOAT, false, 0, 0);

        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.id_i);

        var pMatrix = mat4.create();
        mat4.perspective(45, gl.viewportWidth / gl.viewportHeight, 0.1, 100.0, pMatrix);

        var mvMatrix = mat4.create();
        mat4.identity(mvMatrix);

        mat4.translate(mvMatrix, [this.x, this.y, -10.0]);
        mat4.rotate(mvMatrix, 3.1415 * this.rot, this.axis_rot);

        if (this.mirror_h) {
            mat4.scale(mvMatrix, [-1.0, 1.0, 1.0]);
        }
        if (this.mirror_v) {
            mat4.scale(mvMatrix, [1.0, -1.0, 1.0]);
        }

        gl.uniformMatrix4fv(shaderProgram.pMatrixUniform, false, pMatrix);
        gl.uniformMatrix4fv(shaderProgram.mvMatrixUniform, false, mvMatrix);

        gl.drawElements(gl.TRIANGLES, this.size_i * 3, gl.UNSIGNED_SHORT, 0);
    }
}

class Triangle extends Object {
    constructor(width, height) {
        super("Triangle");

        this.width = width;
        this.height = height;

        this.vertices = [
            0.0, height, 0.0,
            -width * 0.5, -width * 0.5, 0.0,
            width * 0.5, -width * 0.5, 0.0
        ]

        this.colors = [
            1.0, 0.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, 0.0, 1.0
        ]

        this.indices = [
            0, 1, 2
        ]

        this.size_v = 3;
        this.size_c = 3;
        this.size_i = 1;

        this.createBuffers();
    }
}

class Quad extends Object {
    constructor(width) {
        super("Quad");

        this.width = width;

        this.vertices = [
            -width * 0.5, -width * 0.5, 0.0,
            width * 0.5, -width * 0.5, 0.0,
            width * 0.5, width * 0.5, 0.0,
            -width * 0.5, width * 0.5, 0.0
        ]

        this.colors = [
            1.0, 0.0, 0.0,
            0.0, 0.0, 0.0,
            0.0, 0.0, 1.0,
            1.0, 1.0, 1.0
        ]

        this.indices = [
            0, 1, 2,
            2, 3, 0
        ]

        this.size_v = 4;
        this.size_c = 4;
        this.size_i = 2;

        this.createBuffers();
    }
}

class Cube extends Object {
    constructor(width) {
        super("Cube");

        this.width = width;

        this.vertices = [
            -width * 0.5, -width * 0.5, -width * 0.5,
            width * 0.5, -width * 0.5, -width * 0.5,
            width * 0.5, width * 0.5, -width * 0.5,
            -width * 0.5, width * 0.5, -width * 0.5,

            -width * 0.5, -width * 0.5, width * 0.5,
            width * 0.5, -width * 0.5, width * 0.5,
            width * 0.5, width * 0.5, width * 0.5,
            -width * 0.5, width * 0.5, width * 0.5,
        ]

        this.indices = [
            0, 1, 3, 3, 1, 2,
            1, 5, 2, 2, 5, 6,
            5, 4, 6, 6, 4, 7,
            4, 0, 7, 7, 0, 3,
            3, 2, 7, 7, 2, 6,
            4, 5, 0, 0, 5, 1
        ]

        this.size_v = 8;
        this.size_i = 12;

        this.createBuffers();
    }
}