/*
	MAYUSCULAS = Giro 90 grados sentido horario
	minusculas = Giro 90 grados sentido antihorario

	FACE & SLICE ROTATION COMMANDS

	U 	Up
	E 	Equator (rotate according to Up Face's orientation)
	D 	Down

	F	Front
	S 	Standing (rotate according to Front Face's orientation)
	B 	Back

	L 	Left
	M 	Middle (rotate according to Left Face's orientation)
	R 	Right

	CUBE ROTATION

	X   Rotate entire cube according to Right Face's orientation
	Y   Rotate entire cube according to Up Face's orientation
	Z   Rotate entire cube according to Front Face's orientation
*/


$(document).ready(function() {
	// -------------------- cubejs --------------------
	cubeTwoPhase = new Cube();
	Cube.initSolver();

	// -------------------- cuber --------------------
	var useLockedControls = true,
		controls = useLockedControls ? ERNO.Locked : ERNO.Freeform;

	var ua = navigator.userAgent,
		isIe = ua.indexOf('MSIE') > -1 || ua.indexOf('Trident/') > -1;

	window.cubeGL = new ERNO.Cube({
		hideInvisibleFaces: true,
		controls: controls,
		renderer: isIe ? ERNO.renderers.IeCSS3D : null
	});

	const container = document.getElementById( 'container' );
	container.appendChild( cubeGL.domElement );

	if (controls === ERNO.Locked) {
		const fixedOrientation = new THREE.Euler(Math.PI * 0.1, Math.PI * -0.25, 0);
		cubeGL.object3D.lookAt(cubeGL.camera.position);
		cubeGL.rotation.x += fixedOrientation.x;
		cubeGL.rotation.y += fixedOrientation.y;
		cubeGL.rotation.z += fixedOrientation.z;
	}
	cubeGL.twistDuration = 300;
	cubeGL.twist('xY');
})
