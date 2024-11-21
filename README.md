# Trabalho de Sistemas Operacionais - Projeto de Comunicação por Socket

<p>
    Este projeto foi desenvolvido durante as aulas de <strong>Sistemas Operacionais</strong> e implementa um sistema de comunicação por 
    <strong>sockets</strong> que permite a interação entre múltiplos clientes e um servidor. 
    O objetivo é explorar conceitos de <strong>redes</strong>, <strong>concorrência</strong> e <strong>interações cliente-servidor</strong>.
</p>

---

## Funcionalidades Implementadas

### 1. Servidor Multicliente
<ul>
    <li>Permite que múltiplos clientes se conectem simultaneamente.</li>
    <li>Gerencia conexões utilizando threads para a eficiência </li>
</ul>

### 2. Envio de Mensagens
<ul>
    <li>Os clientes podem enviar mensagens de texto que são retransmitidas para todos os outros clientes conectados.</li>
</ul>

### 3. Comandos Remotos
<ul>
    <li><strong>Desligar monitor:</strong> O servidor executa comandos que permitem desligar o monitor do cliente.</li>
    <li><strong>Executar scripts:</strong> Scripts em Python podem ser executados remotamente no cliente.</li>
</ul>

### 4. Transmissão de Vídeo
<ul>
    <li>O servidor suporta a transmissão de frames de vídeo capturados pela webcam, permitindo que os clientes visualizem a transmissão.</li>
</ul>

### 5. Interação com Aplicativos
<ul>
    <li>Os clientes podem instalar e executar aplicativos remotamente enviando comandos específicos ao servidor.</li>
</ul>

---

## Tecnologias Utilizadas

### Python
<ul>
    <li><strong>Servidor:</strong>
        <ul>
            <li>Implementado com suporte a threads para gerenciar conexões.</li>
            <li>Manipulação de recursos locais, como webcam e execução de comandos do sistema operacional.</li>
            <li><strong>Bibliotecas:</strong> <code>socket</code>, <code>threading</code>, <code>ctypes</code>.</li>
        </ul>
    </li>
</ul>

### Node.js
<ul>
    <li><strong>Cliente:</strong>
        <ul>
            <li>Implementação interativa que permite comunicação e execução de tarefas remotas.</li>
            <li><strong>Bibliotecas:</strong> <code>net</code>, <code>readline</code>, <code>node-webcam</code>.</li>
        </ul>
    </li>
</ul>

---

## Como Executar

### 1. Clonar o Repositório
```bash
git clone https://github.com/jvitorr13/Trabalho_Socket.git
cd Trabalho_Socket
