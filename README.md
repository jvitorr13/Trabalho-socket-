Trabalho de Sistemas Operacionais - Projeto de Comunicação por Socket
Este projeto foi desenvolvido durante as aulas de Sistemas Operacionais e implementa um sistema de comunicação por sockets que permite a interação entre múltiplos clientes e um servidor. O foco é explorar conceitos de redes, concorrência e interações cliente-servidor.

Funcionalidades Implementadas
Servidor Multicliente:

Permite que múltiplos clientes se conectem simultaneamente.
Gerencia conexões usando threads.
Envio de Mensagens:

Os clientes podem enviar mensagens de texto que são retransmitidas para todos os demais clientes conectados.
Comandos Remotos:

Desligar monitor: O servidor executa comandos para desligar o monitor do cliente.
Executar scripts: Scripts em Python podem ser executados remotamente.
Transmissão de Vídeo:

O servidor suporta transmissão de frames de vídeo capturados pela webcam.
Interação com Aplicativos:

Os clientes podem instalar e executar aplicativos remotamente via comandos.
Tecnologias Utilizadas
Python:
Servidor implementado com suporte a threads para gerenciar conexões.
Manipulação de recursos locais como webcam e execução de comandos do sistema operacional.
Node.js:
Cliente interativo com opções para comunicação e execução de tarefas remotas.
Bibliotecas:
socket, threading, ctypes (Python).
net, readline, node-webcam (Node.js).
