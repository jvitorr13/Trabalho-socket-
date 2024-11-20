<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trabalho de Sistemas Operacionais - Projeto de Comunicação por Socket</title>
</head>
<body>
    <h1>Trabalho de Sistemas Operacionais - Projeto de Comunicação por Socket</h1>
    <p>
        Este projeto foi desenvolvido durante as aulas de <strong>Sistemas Operacionais</strong> e implementa um sistema de comunicação por 
        <strong>sockets</strong> que permite a interação entre múltiplos clientes e um servidor. 
        O objetivo é explorar conceitos de <strong>redes</strong>, <strong>concorrência</strong> e <strong>interações cliente-servidor</strong>.
    </p>

    <hr>

    <h2>Funcionalidades Implementadas</h2>
    <h3>1. Servidor Multicliente</h3>
    <ul>
        <li>Permite que múltiplos clientes se conectem simultaneamente.</li>
        <li>Gerencia conexões utilizando threads para garantir eficiência e paralelismo.</li>
    </ul>

    <h3>2. Envio de Mensagens</h3>
    <ul>
        <li>Os clientes podem enviar mensagens de texto que são retransmitidas para todos os outros clientes conectados.</li>
    </ul>

    <h3>3. Comandos Remotos</h3>
    <ul>
        <li><strong>Desligar monitor:</strong> O servidor executa comandos que permitem desligar o monitor do cliente.</li>
        <li><strong>Executar scripts:</strong> Scripts em Python podem ser executados remotamente no cliente.</li>
    </ul>

    <h3>4. Transmissão de Vídeo</h3>
    <ul>
        <li>O servidor suporta a transmissão de frames de vídeo capturados pela webcam, permitindo que os clientes visualizem a transmissão.</li>
    </ul>

    <h3>5. Interação com Aplicativos</h3>
    <ul>
        <li>Os clientes podem instalar e executar aplicativos remotamente enviando comandos específicos ao servidor.</li>
    </ul>

    <hr>

    <h2>Tecnologias Utilizadas</h2>
    <h3>Python</h3>
    <ul>
        <li><strong>Servidor:</strong>
            <ul>
                <li>Implementado com suporte a threads para gerenciar conexões.</li>
                <li>Manipulação de recursos locais, como webcam e execução de comandos do sistema operacional.</li>
                <li><strong>Bibliotecas:</strong> <code>socket</code>, <code>threading</code>, <code>ctypes</code>.</li>
            </ul>
        </li>
    </ul>

    <h3>Node.js</h3>
    <ul>
        <li><strong>Cliente:</strong>
            <ul>
                <li>Implementação interativa que permite comunicação e execução de tarefas remotas.</li>
                <li><strong>Bibliotecas:</strong> <code>net</code>, <code>readline</code>, <code>node-webcam</code>.</li>
            </ul>
        </li>
    </ul>

    <hr>

    <h2>Como Executar</h2>
    <h3>1. Clonar o Repositório</h3>
    <pre>
<code>
git clone https://github.com/jvitorr13/Trabalho_Socket.git
cd Trabalho_Socket
</code>
    </pre>

    <h3>2. Executar o Servidor</h3>
    <p>
        Navegue até o diretório do servidor e execute:
    </p>
    <pre>
<code>
python servidor.py
</code>
    </pre>

    <h3>3. Executar o Cliente</h3>
    <p>
        Navegue até o diretório do cliente e execute:
    </p>
    <pre>
<code>
node cliente.js
</code>
    </pre>

    <h3>4. Interagir</h3>
    <ul>
        <li>Insira o nome no cliente.</li>
        <li>Escolha as opções disponíveis no menu para enviar mensagens, executar comandos remotos ou visualizar a transmissão de vídeo.</li>
    </ul>

    <hr>

    <h2>Conclusão</h2>
    <p>
        Este projeto reforça conceitos importantes de <strong>redes</strong>, <strong>sistemas distribuídos</strong> e 
        <strong>programação concorrente</strong>, permitindo a integração de diferentes linguagens e ferramentas em um sistema funcional. 
        Ele é uma base sólida para entender como criar aplicações de comunicação em tempo real usando sockets.
    </p>
</body>
</html>
