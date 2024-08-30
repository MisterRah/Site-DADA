document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.flash-message');
    
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.style.opacity = 0;
            setTimeout(function() {
                message.style.display = 'none'; // Remove o elemento do layout
            }, 500);  // Tempo para a transição de opacidade
        }, 1500);  // Tempo antes da mensagem começar a desaparecer
    });
});