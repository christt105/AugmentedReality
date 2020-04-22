class Object {
    constructor(type) {
        this.type = type;

        this.x = 0.0;
        this.y = 0.0;

        this.rot = 0.0;
        this.axis_rot = [0.0, 0.0, 1.0];

        this.mirror_h = false;
        this.mirror_v = false;
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
        this.type.bindBuffers();

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