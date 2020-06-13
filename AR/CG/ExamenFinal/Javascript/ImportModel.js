function loadModel(name) {
    var model = {};
    var request = new XMLHttpRequest();
    var path = "models/" + name + ".json";

    request.open("GET", path);
    request.onreadystatechange = function () {
        if (request.readyState == 4) {
            handleLoadedModel(model, JSON.parse(request.responseText));
        }
    }
    request.send();
    return model;
}

function handleLoadedModel(model, modelData) {
    //Vertex Buffer
    model.vertexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, model.vertexBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(modelData.vertexPositions), gl.STATIC_DRAW);
    model.vertexBuffer.itemSize = 3;
    model.vertexBuffer.numItems = modelData.vertexPositions.length / 3;

    //Index Buffer
    model.indexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, model.indexBuffer);
    gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(modelData.indices), gl.STATIC_DRAW);
    model.indexBuffer.itemSize = 1;
    model.indexBuffer.numItems = modelData.indices.length;

    //Normals Buffer
    model.normalBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, model.normalBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(modelData.vertexNormals), gl.STATIC_DRAW);
    model.normalBuffer.itemSize = 3;
    model.normalBuffer.numItems = modelData.vertexNormals.length / 3;

    //Texture Buffer
    // model.textureBuffer = gl.createBuffer();
    // gl.bindBuffer(gl.ARRAY_BUFFER, model.textureBuffer);
    // gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(modelData.vertexTextureCoords), gl.STATIC_DRAW);
    // model.textureBuffer.itemSize = 2;
    // model.textureBuffer.numItems = modelData.vertexTextureCoords.length / 2;
}