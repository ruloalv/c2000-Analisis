function toggleSubMenu(submenuId) {
    const submenu = document.getElementById(submenuId);
    console.log(submenuId);
    submenu.style.display = submenu.style.display === 'none' || submenu.style.display === '' ? 'block' : 'none';
}

// document.addEventListener("DOMContentLoaded", function () {
//     // Obtener elementos del menú
//     const submenuLinks = document.querySelectorAll(".submenu-link");

//     submenuLinks.forEach(link => {
//         link.addEventListener("click", function (event) {
//             event.preventDefault();
//             const url = event.target.getAttribute("href");

//             fetch(url)
//                 .then(response => response.text())
//                 .then(data => {
//                     document.getElementById("main-content").innerHTML = data;
//                 })
//                 .catch(error => console.error("Error al cargar el contenido:", error));
//         });
//     });
// });
