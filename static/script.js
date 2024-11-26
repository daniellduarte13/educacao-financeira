// Desenvolvido por Daniel Jozias. Aluno do 3º X - CEMEP
// script.js

// Efeito de hover para os links da navbar
const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

navLinks.forEach(link => {
    link.addEventListener('mouseover', () => {
        link.style.color = '#ff9d00'; // Muda a cor ao passar o mouse
    });

    link.addEventListener('mouseout', () => {
        link.style.color = '#ffffff'; // Retorna à cor original
    });
});

// Animação do botão de contato
const contatoButton = document.querySelector('.botao-contato');

contatoButton.addEventListener('mouseover', () => {
    contatoButton.style.backgroundColor = '#FFD700'; // Muda a cor ao passar o mouse
    contatoButton.style.transform = 'translateY(-3px)'; // Levanta o botão
});

contatoButton.addEventListener('mouseout', () => {
    contatoButton.style.backgroundColor = '#FFA500'; // Retorna à cor original
    contatoButton.style.transform = 'translateY(0)'; // Retorna à posição original
});

// Mantém o dropdown aberto se algum item dentro dele estiver ativo
document.addEventListener('DOMContentLoaded', () => {
    const activeDropdownItem = document.querySelector('.dropdown-item.active');
    if (activeDropdownItem) {
        const dropdownToggle = activeDropdownItem.closest('.dropdown').querySelector('.nav-link');
        dropdownToggle.classList.add('active');
    }
});

// Função para gerar uma cor RGB aleatória
function getRandomRGB() {
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    return `rgb(${r}, ${g}, ${b})`;
}

// Aplica o efeito RGB ao botão "Rede Social"
document.addEventListener('DOMContentLoaded', () => {
    const redeSocialButton = document.querySelector('.rede-social-button');
    if (redeSocialButton) {
        setInterval(() => {
            redeSocialButton.style.backgroundColor = getRandomRGB();
        }, 1000); // Muda a cor a cada segundo
    }
});
