from telegram import Update
from telegram.ext import Updater, CommandHandler



# /start
def start(update: Update, context):
    update.message.reply_text(
        "🔥 **Fala, torcedor da FURIA!** 🔥\n\n"
        "Bem-vindo ao FURIOSO GG BOT — o bot mais agressivo do cenário! 💥\n"
        "Aqui você encontra tudo sobre a FURIA no CS 2! 🎮\n\n"
        "Use os comandos abaixo para ficar por dentro de tudo:\n\n"
        "📋 **/lineup** → Veja a escalação atual da FURIA\n"
        "📅 **/agenda** → Confira os próximos confrontos da nossa line\n"
        "🎮 **/lastmatch** → Última partida da FURIA\n"
        "📰 **/noticias** → Últimas notícias sobre a FURIA\n"
        "💡 **/curiosidade** → Curiosidade sobre a FURIA\n"
        "📲 **/social** → Links para nossas redes sociais oficiais\n"
        "🗺 **/mapa** → Winrates da FURIA por mapa"
    )

# /lineup
def lineup(update: Update, context):
    update.message.reply_text(
        " Line-Up Atual da FURIA (CS2) 💥\n\n"
        "Confira os monstros que estão dominando o cenário do CS 2:\n\n"
        "1. **Fallen** 🔫 - IGL e líder nato, não tem o que falar do professor, a não ser, PRESENTE!!\n"
        "2. **yuurih** ⚡ - Rifler veloz, um dos **principais destaques** da FURIA, sempre preciso.\n"
        "3. **KSCERATO** 🏹 - Master of Clutches, um dos melhores jogadores do CS, sempre decisivo.\n"
        "4. **Molodoy** 🎯 - O jovem prodígio ucraniano foi contratado para reforçar a posição de AWP da equipe e dá muita bala\n"
        "5. **Yekindar** 🎮 - YEKINDAR foi adicionado temporariamente à line-up e mostrou para o que veio, atuando até o final do BLAST.tv Major: Austin 2025."
    )

# /agenda
def agenda(update: Update, context):
    update.message.reply_text(
        "📅 Próximos Confrontos da FURIA 🔥\n\n"
        "🔥 **FURIA VS COMPLEXITY GAMER** - 27/04/2025 ⚔️\n"
        "🔥 **FURIA vs TEAM LIQUID** - 29/04/2025 — A batalha épica que todos estão esperando! 💥\n\n"
        "⚔️ Não perca! A FURIA está em ação nos maiores palcos do CS 2!"
    )

# /lastmatch
def lastmatch(update: Update, context):
    update.message.reply_text(
        "🎮 **Última Partida da FURIA** 🏆\n\n"
        "🔹 **FURIA 1 - 2 Falcons** (21/03/2025)\n"
        " Infelizmente dessa vez não deu, a furia caiu pra poderosa Falcons e foi eliminada do ESl Pro League.🏅\n"
        "💪 Voltaremos mais fortes do que nunca, a FURIA segue sendo a tropa mais braba do servidor e não vai parar de lutar!"
    )

# /noticias
def noticias(update: Update, context):
    update.message.reply_text(
        "📰 **Últimas Notícias da FURIA** 🚨\n\n"
        "- FURIA garante vaga nos playoffs do Major! 💣 Eles seguem imparáveis!\n"
        "- Novo reforço: saffee brilha como AWP titular e já é destaque! 🔥\n"
        "- arT revela suas novas táticas para maps como Overpass! 💡\n\n"
        "Fique ligado, a FURIA não para de surpreender! 😎"
    )

# /curiosidade
def curiosidade(update: Update, context):
    update.message.reply_text(
        "💡 **Curiosidade FURIA** 🤔\n\n"
        "Você sabia que a FURIA tem uma das maiores porcentagens de entry kills no mundo? 🔥\n"
        "A agressividade da equipe é referência e tem sido copiada por times de todo o mundo! 🌍\n"
        "Isso mostra o quanto a FURIA está dominando o cenário competitivo! 🏆"
    )

# /social
def social(update: Update, context):
    update.message.reply_text(
        "📲 **Redes Sociais Oficiais da FURIA** 🌐\n\n"
        "🔗 **Instagram**: [@furiaesports](https://instagram.com/furiaesports)\n"
        "🔗 **Twitter**: [@furia](https://twitter.com/furia)\n"
        "🔗 **YouTube**: [FURIA Esports](https://www.youtube.com/c/FURIAEsports)\n"
        "🔗 **Discord**: [FURIA](https://discord.gg/furia)\n\n"
        "Fique por dentro de tudo o que rola nos **bastidores da FURIA**! 🔥"
    )

# /mapa
def mapa(update: Update, context):
    update.message.reply_text(
        "🗺 **Winrates por Mapa (últimos 3 meses)** 📊\n\n"
        "- **Mirage**: 75% 🌆 — O mapa onde a FURIA brilha com táticas insanas! 💥\n"
        "- **Inferno**: 70% 🔥 — Aqui, a FURIA se impõe com estratégias perfeitas.\n"
        "- **Ancient**: 68% 🏛️ — Excelente performance em um mapa difícil.\n"
        "- **Nuke**: 60% ☢️ — Um dos mapas mais desafiadores, mas a FURIA não se intimida!\n"
        "- **Vertigo**: 55% 🏗️ — Ainda trabalhando para melhorar, mas com grandes potenciais!\n\n"
        "A FURIA domina o cenário e seus winrates provam isso!"
    )

# Inicializador do bot
def main():
    token = "7547878261:AAHVkiLFz6o0wd2nck7tQ8g2p24hB7U-n2s"

    updater = Updater(token)
    dispatcher = updater.dispatcher

    # Comandos visíveis no Telegram
    updater.bot.set_my_commands([
        ('start', 'Boas-vindas e menu'),
        ('lineup', 'Escalação atual'),
        ('agenda', 'Próximos jogos'),
        ('lastmatch', 'Última partida'),
        ('noticias', 'Últimas notícias'),
        ('curiosidade', 'Curiosidades da FURIA'),
        ('social', 'Redes sociais oficiais'),
        ('mapa', 'Winrates por mapa')
    ])

    # Ligar os comandos às funções
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("lineup", lineup))
    dispatcher.add_handler(CommandHandler("agenda", agenda))
    dispatcher.add_handler(CommandHandler("lastmatch", lastmatch))
    dispatcher.add_handler(CommandHandler("noticias", noticias))
    dispatcher.add_handler(CommandHandler("curiosidade", curiosidade))
    dispatcher.add_handler(CommandHandler("social", social))
    dispatcher.add_handler(CommandHandler("mapa", mapa))

    # Iniciar o bot
    updater.start_polling()
    updater.idle()

# Executa o bot
if __name__ == '__main__':
    main()

import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")



