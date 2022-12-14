from telegram.ext import *
from telegram_bot_inter import TelegramBotInterface
import keys

from user import User
from datetime import date



class TelegramFoodOrder(TelegramBotInterface):

    def __init__(self):
        self.user = User()

    def start_command(self, update, context):
        update.message.reply_text('Hello there! I\'m a food orderer bot \n first you will need to enter your credit card details .')

    def help_command(self, update, context):
        update.message.reply_text('I can order pizza, toast and falafel for you ,but only one time a day!\n'
                                  'All you need to do is to set your credit card details , select food  '
                                  'and I will do all the rest\n'
                                  'The format of the commands are :\n'
                                  '/name <name>\n'
                                  '/card_number <number>\n'
                                  '/cv <cv>\n'
                                  '/card_date <xx/xx/xxxx>\n'
                                  '/pizza\n'
                                  '\\toast\n'
                                  '\\falafel\n')

    def set_name(self, update, context):
        name=self.user.set_name(update)
        if name==update:
            send_message("Name updated", update)
        else:
            send_message("Error occured",update)
    def set_card_number(self, update, context):
        card_number=self.user.set_card_number(update)
        if card_number==update:
            send_message("Card number updated", update)
        else:
            send_message("Error occured",update)
    
    def set_cv(self, update, context):
        cv=self.user.set_cv(update)
        if cv==update:
            send_message("cv updated", update)
        else:
            send_message("Error occured",update)

    def set_card_date(self, update, context):
        date=self.user.set_card_date(update)
        if date==update:
            send_message("card date updated", update)
        else:
            send_message("Error occured",update)

    def order_pizza(self, update, context):
       if date.today()!= self.user.last_order:
            self.user.set_last_order(date.today())
            send_message("I ordered pizza for you",update)
       else:
           send_message("you can only order once a day", update)

    def order_falafel(self, update, context):
       if date.today()!= self.user.last_order:
            self.user.set_last_order(date.today())
            send_message("I ordered falafel for you",update)
       else:
           send_message("you can only order once a day", update)
    
    def order_falafel(self, update, context):
       if date.today()!= self.user.last_order:
            self.user.set_last_order(date.today())
            send_message("I oredered toast for you",update)
       else:
           send_message("you can only order once a day", update)

def send_message(text, update):
    
    update.message.reply_text(text)



# Run the program
if __name__ == '__main__':
    print('Starting up bot...')
    bot = TelegramFoodOrder()

    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    # handling commands 
    dp.add_handler(CommandHandler('start', bot.start_command))
    dp.add_handler(CommandHandler('help', bot.help_command))
    dp.add_handler(CommandHandler('name', bot.set_name))
    dp.add_handler(CommandHandler('card_number', bot.set_card_number))
    dp.add_handler(CommandHandler('cv', bot.set_cv))
    dp.add_handler(CommandHandler('card_date', bot.set_card_date))
    dp.add_handler(CommandHandler('pizza', bot.order_pizza))
    dp.add_handler(CommandHandler('falafel', bot.order_falafel))
    dp.add_handler(CommandHandler('toast', bot.order_toast))

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
