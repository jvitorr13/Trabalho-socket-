const net = require('net');
const readline = require('readline');
const { exec } = require('child_process');
const NodeWebcam = require('node-webcam');

// entrada de dados via terminal
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


rl.question('Digite seu nome: ', (nome) => {
    const client = new net.Socket();
    client.connect(5000, '127.0.0.1', () => {
        console.log(`Conectado ao servidor como ${nome}`);
        client.write(nome); // Envia o nome ao servidor
        exibirMenu(client);
    });

    // Recebe mensagens do servidor
    client.on('data', (data) => {
        console.log(`Servidor: ${data.toString()}`);
    });

    client.on('close', () => {
        console.log('Desconectado do servidor.');
        process.exit(0);
    });
});

function exibirMenu(client) {
    console.log("\nSelecione uma opção:");
    console.log("1 - Enviar mensagens (modo contínuo)");
    console.log("2 - Inverter movimento do mouse");
    console.log("3 - Limitar movimento do mouse");
    console.log("4 - Desligar monitor remotamente");
    console.log("5 - Iniciar transmissão de vídeo da webcam");
    console.log("6 - Instalar e rodar um aplicativo remoto");
    console.log("7 - Sair\n");

    rl.question("Escolha uma opção: ", (opcao) => {
        processarOpcao(opcao.trim(), client);
    });
}

function processarOpcao(opcao, client) {
    switch (opcao) {
        case '1':
            iniciarEnvioDeMensagens(client);
            break;
        case '2':
            executarScript('Inverter_Mouse.py', "Inversão do mouse realizada.");
            exibirMenu(client);
            break;
        case '3':
            executarScript('Limitar_Movimento.py', "Limite de movimento do mouse ajustado.");
            exibirMenu(client);
            break;
        case '4':
            client.write('/desligar_monitor');
            console.log("Comando para desligar monitor enviado!");
            exibirMenu(client);
            break;
        case '5':
            openWebcam(() => exibirMenu(client));
            break;
        case '6':
            rl.question("Digite o nome do aplicativo para instalar e rodar: ", (appName) => {
                instalarERodarAplicativo(appName, () => exibirMenu(client));
            });
            break;
        case '7':
            console.log("Encerrando conexão...");
            client.end();
            rl.close();
            break;
        default:
            console.log("Opção inválida. Tente novamente.");
            exibirMenu(client);
            break;
    }
}

function iniciarEnvioDeMensagens(client) {
    console.log("Digite suas mensagens (ou 'sair' para voltar ao menu):");
    rl.on('line', (input) => {
        if (input.trim().toLowerCase() === 'sair') {
            rl.removeAllListeners('line');
            exibirMenu(client);
        } else {
            client.write(input);
        }
    });
}

function executarScript(scriptName, successMessage) {
    exec(`python ${scriptName}`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Erro ao executar ${scriptName}: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
        }
        console.log(successMessage);
        console.log(`stdout: ${stdout}`);
    });
}

function instalarERodarAplicativo(appName, callback) {
    exec(`python gerenciar_app.py ${appName}`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Erro ao instalar/executar o aplicativo: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
        }
        console.log(`Aplicativo ${appName} instalado e executado.`);
        console.log(`stdout: ${stdout}`);
        callback();
    });
}

function openWebcam(callback) {
    console.log('Abrindo a webcam...');
    NodeWebcam.capture("webcam_image", {}, (err, data) => {
        if (err) {
            console.error('Erro ao abrir a webcam: ', err);
        } else {
            console.log('Webcam aberta com sucesso! Veja a imagem gerada.');
        }
        callback();
    });
}
