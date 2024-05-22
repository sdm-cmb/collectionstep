// Selecione o botão do menu e os botões da cascata
const menuButton = document.getElementById('menu-button');
const buttonCascade = document.querySelector('.button-cascade');
// Defina uma variável para rastrear o estado do menu
let isMenuOpen = false;
// Adicione um ouvinte de evento de clique ao botão do menu
menuButton.addEventListener('click', function(event) {
    // Evite o comportamento padrão do botão
    event.initEvent();
    // Alterne a classe 'hidden' nos botões da cascata ao clicar no botão do menu
    buttonCascade.classList.toggle('click');
 
    // Alterne o estado do menu
    isMenuOpen = !isMenuOpen;
    // Ajuste a opacidade e a altura máxima para animação suave
    if (isMenuOpen) {
        buttonCascade.style.opacity = '1';
        buttonCascade.style.maxHeight = '200px'; // Ajuste conforme necessário
    } else {
        buttonCascade.style.opacity = '0';
        buttonCascade.style.maxHeight = '0';
    }
});
// Adicione um ouvinte de evento de clique ao documento para fechar o menu ao clicar fora dele
document.addEventListener('click', function(event) {
    if (!menuButton.contains(event.target) && !buttonCascade.contains(event.target)) {
        // Verifique se o clique não foi no botão do menu ou nos botões da cascata
        buttonCascade.classList.add('click');
        isMenuOpen = false;
        buttonCascade.style.opacity = '0';
        buttonCascade.style.maxHeight = '0';
    }
})