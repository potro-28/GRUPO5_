document.getElementById("registerForm").addEventListener("submit", function(e) {
  e.preventDefault(); // Evita que recargue la página automáticamente

  // Obtener valores de los campos
  const name = document.getElementById("name").value.trim();
  const correo = document.getElementById("correoLogin").value.trim();
  const password = document.getElementById("passwordLogin").value.trim();
  const confirmPassword = document.getElementById("confirmPassword").value.trim();

  // Validaciones básicas
  if (password !== confirmPassword) {
    alert("Las contraseñas no coinciden ");
    return;
  }

  if (name === "" || correo === "" || password === "" || confirmPassword === "") {
    alert("Por favor completa todos los campos.");
    return;
  }

  // Simulación de registro exitoso
  alert("Registro exitoso 🎉 Bienvenido/a " + name);

  //  Redirigir al menú (ruta relativa)
      window.location.href = "../menudeusuario/menu.html";
});
// Función para mostrar/ocultar contraseña
function togglePassword(id, el) {
  const input = document.getElementById(id);

  if (input.type === "password") {
    input.type = "text";
    el.classList.remove("fa-eye");
    el.classList.add("fa-eye-slash");
  } else {
    input.type = "password";
    el.classList.remove("fa-eye-slash");
    el.classList.add("fa-eye");
  }
}

