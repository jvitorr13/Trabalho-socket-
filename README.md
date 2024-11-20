Trabalho de Sistemas Operacionais - Projeto de Comunicação por Socket
Este projeto foi desenvolvido durante as aulas de Sistemas Operacionais e implementa um sistema de comunicação por sockets que permite a interação entre múltiplos clientes e um servidor. O objetivo é explorar conceitos de redes, concorrência e interações cliente-servidor.

Funcionalidades Implementadas
1. Servidor Multicliente
Permite que múltiplos clientes se conectem simultaneamente.
Gerencia conexões utilizando threads para garantir eficiência e paralelismo.
2. Envio de Mensagens
Os clientes podem enviar mensagens de texto que são retransmitidas para todos os outros clientes conectados.
3. Comandos Remotos
Desligar monitor: O servidor executa comandos que permitem desligar o monitor do cliente.
Executar scripts: Scripts em Python podem ser executados remotamente no cliente.
4. Transmissão de Vídeo
O servidor suporta a transmissão de frames de vídeo capturados pela webcam, permitindo que os clientes visualizem a transmissão.
5. Interação com Aplicativos
Os clientes podem instalar e executar aplicativos remotamente enviando comandos específicos ao servidor.
Tecnologias Utilizadas
Python
Servidor:
Implementado com suporte a threads para gerenciar conexões.
Manipulação de recursos locais, como webcam e execução de comandos do sistema operacional.
Bibliotecas: socket, threading, ctypes.
Node.js
Cliente:
Implementação interativa que permite comunicação e execução de tarefas remotas.
Bibliotecas: net, readline, node-webcam.
