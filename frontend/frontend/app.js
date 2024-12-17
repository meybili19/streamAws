window.onload = async function() {
  // Obtener la información de la instancia EC2 desde el backend
  const response = await fetch('http://localhost:5000/stream-info');
  const data = await response.json();

  // Mostrar IP y Localización
  document.getElementById('ip').textContent = data.ip;
  document.getElementById('location').textContent = `${data.location.city}, ${data.location.country}`;

  // Simulación de "encender" la cámara o video
  const videoElement = document.getElementById('video');
  videoElement.play();
};
