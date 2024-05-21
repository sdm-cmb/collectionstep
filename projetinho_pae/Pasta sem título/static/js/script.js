// Selecione o botão do menu e os botões da cascata
const menuButton = document.getElementById('menu-button');
const buttonCascade = document.querySelector('.button-cascade');

// Adicione um ouvinte de evento de clique ao botão do menu
menuButton.addEventListener('click', function() {
    // Alterne a classe 'hidden' nos botões da cascata ao clicar no botão do menu
    buttonCascade.classList.toggle('hidden');
});
