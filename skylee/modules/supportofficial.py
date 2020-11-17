import speedtest
import requests
import datetime
import platform

from psutil import cpu_percent, virtual_memory, disk_usage, boot_time
from platform import python_version
from telegram import __version__
from spamwatch import __version__ as __sw__
from pythonping import ping as ping3
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from skylee import dispatcher, OWNER_ID
from skylee.modules.helper_funcs.filters import CustomFilters
from skylee.modules.helper_funcs.alternate import typing_action


@run_async
@typing_action
def admin_list(update, context):
    support = STAFF UFFICIALE DEL BOT
    support = owner e gestore codice 👑: @doggycheems 
    support = Gestori fedban⛔️: @doggycheems @marvynstar @TheDarknessCatGty @Camminatoredeighiacci @lEGIONARIO_ROMANO\n"

    support = Supporter👍: @marvynstar @TheDarknessCatGty @Camminatoredeighiacci @lEGIONARIO_ROMANO\n"
    support = ATTENZIONE\n"
    support = Il bot è in fase di beta testing ed è disponibile solo per gruppi di @doggycheems o autorizzati\n"
    support = Vuoi essere beta tester? scrivi a @doggycheems e chiedi ti darà tutti i dettagli necessari\n"
    support = context.bot.sendMessage(update.effective_chat.id, support, parse_mode=ParseMode.HTML)

ADMIN_LIST_HANDLER = CommandHandler(
    "staffbot", admin_list, filters=CustomFilters.sudo_filter
)

dispatcher.add_handler(ADMIN_LIST_HANDLER)
