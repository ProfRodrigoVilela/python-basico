document.getElementById('btn-acao').addEventListener('click', function() {
    const mensagem = document.getElementById('mensagem');
    mensagem.textContent = 'JavaScript funcionando! O versionamento está dando certo.';
    mensagem.style.color = '#0056b3';
    mensagem.style.fontWeight = 'bold';
    mensagem.style.marginTop = '15px';
});