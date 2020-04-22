class Mesh {
    constructor(name) {
        this.name = name;
    }

    createBuffers() {
        this.createVertexBuffer(this.vertices, this.colors);
        this.createIndexBuffer(this.indices);
        
    }

    createVertexBuffer(vertices, colors) {
        this.id_v = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, this.id_v);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);
    }

    createIndexBuffer(indices) {
        this.id_i = gl.createBuffer();
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.id_i);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(indices), gl.STATIC_DRAW)
    }

    bindBuffers() {
        gl.bindBuffer(gl.ARRAY_BUFFER, this.id_v);
        gl.vertexAttribPointer(shaderProgram.vertexPositionAttribute, 3, gl.FLOAT, false, 0, 0);

        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.id_i);
    }

    draw() {
        gl.drawElements(gl.TRIANGLES, this.size_i * 3, gl.UNSIGNED_SHORT, 0);
    }
}

class Triangle extends Mesh {
    constructor(width, height) {
        super("Triangle");

        this.width = width;
        this.height = height;

        this.vertices = [
             0.0,           height,      0.0,
            -width * 0.5,  -width * 0.5, 0.0,
             width * 0.5,  -width * 0.5, 0.0
        ]

        this.indices = [
            0, 1, 2
        ]

        this.size_v = 3;
        this.size_i = 1;

        this.createBuffers();
    }
}

class Quad extends Mesh {
    constructor(width) {
        super("Quad");

        this.width = width;

        this.vertices = [
            -width * 0.5, -width * 0.5, 0.0,
            width * 0.5, -width * 0.5, 0.0,
            width * 0.5, width * 0.5, 0.0,
            -width * 0.5, width * 0.5, 0.0
        ]

        this.indices = [
            0, 1, 2,
            2, 3, 0
        ]

        this.size_v = 4;
        this.size_i = 2;

        this.createBuffers();
    }
}

class Cube extends Mesh {
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