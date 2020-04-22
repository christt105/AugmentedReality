class Object {
    constructor(type, colors) {
        this.type = type;

        this.x = 0.0;
        this.y = 0.0;

        this.rot = 0.0;
        this.axis_rot = [0.0, 0.0, 1.0];

        this.mirror_h = false;
        this.mirror_v = false;

        if (colors != null) {
            this.colors = colors;
        }
        else {
            if (type.name == "Triangle")
                this.sizev = 3;
            else if (type.name == "Quad")
                this.sizev = 4;

            this.colors = new Float32Array(this.sizev * 3);
            this.colors.fill(1.0);
            console.log(this.colors);
        }

        this.createColorVertexBuffer(this.colors);
    }

    createColorVertexBuffer(colors) {
        this.id_c = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, this.id_c);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(colors), gl.STATIC_DRAW);
    }

    setPosition(x, y) {
        this.x = x;
        this.y = y;
    }

    setRotation(rot, axis = [0.0, 0.0, 1.0]) {
        this.rot = rot;
        this.axis_rot = axis;
    }

    setColorVertex(colors) {
        this.colors = colors;
    }

    setMirrorH(value) {
        this.mirror_h = value;
    }

    setMirrorV(value) {
        this.mirror_v = value;
    }

    draw() {
        this.type.bindBuffers();

        gl.bindBuffer(gl.ARRAY_BUFFER, this.id_c);
        gl.vertexAttribPointer(shaderProgram.vertexColorAttribute, 3, gl.FLOAT, false, 0, 0);

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

        this.type.draw();
    }
}