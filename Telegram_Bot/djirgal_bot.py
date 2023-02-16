from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_commands as commands



app = ApplicationBuilder().token("6078286442:AAFtlPvGY8LeEkwUk5d14BLtPuQwjL4_g_Q").build()

app.add_handler(CommandHandler("hi", commands.hi_command))
app.add_handler(CommandHandler("time", commands.time_command))
app.add_handler(CommandHandler("help", commands.help_command))
app.add_handler(CommandHandler("sum", commands.sum_command))

print('server Djirgals Bot started')
app.run_polling()