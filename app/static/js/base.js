function toggleSubMenu(submenuId) {
    const submenu = document.getElementById(submenuId);
    console.log(submenuId);
    submenu.style.display = submenu.style.display === 'none' || submenu.style.display === '' ? 'block' : 'none';
}

//Muestra el formulario vacío para agregar un nuevo proveedor
function showFormNewProveedor() {
    document.getElementById("name").value = "";         // Limpia el campo de nombre
    document.getElementById("location").value = "";     // Limpia el campo de ubicación
    addForm = document.getElementById("add-form")
    addForm.style.display = addForm.style.display === "none" ? "block" : "none";  // Muestra el formulario
  };