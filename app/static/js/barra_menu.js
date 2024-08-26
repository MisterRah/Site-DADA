function menuShow() {
    let menuMobile = document.querySelector('.mobile-menu');
    if (menuMobile.classList.contains('open')) {
        menuMobile.classList.remove('open');
        document.querySelector('.icon').src = "static/img/menu_black.png";
    } else {
        menuMobile.classList.add('open');
        document.querySelector('.icon').src = "static/img/close_black.png";
    }
}

function toggleSubMenu(event) {
    event.preventDefault(); // Previne o comportamento padrão do link
    let subMenu = event.target.nextElementSibling; // Seleciona a sub-menu relacionada
    if (subMenu.classList.contains('open')) {
        subMenu.classList.remove('open');
    } else {
        subMenu.classList.add('open');
    }
}