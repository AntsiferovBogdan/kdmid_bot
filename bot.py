from config import TOKEN
from jobs import parsing
from telegram.ext import Updater

import logging
logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    bot = Updater(TOKEN)

    jq = bot.job_queue
    jq.run_repeating(parsing, interval=900, first=1)

    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
