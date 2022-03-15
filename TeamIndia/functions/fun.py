from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from TeamIndia.__main__ import *


# Buttons Function for fun module


def india_fun_callback(update, context):
    query = update.callback_query
    if query.data == "indiafun_":
        query.message.edit_text(
            text=""" Here is the help for the *Memes* module:

 ❍ /runs: reply a random string from an array of replies
 ❍ /slap: slap a user, or get slapped if not a reply
 ❍ /shrug: get shrug XD
 ❍ /table: get flip/unflip :v
 ❍ /decide: Randomly answers yes/no/maybe
 ❍ /toss: Tosses A coin
 ❍ /bluetext: check urself :V
 ❍ /roll: Roll a dice
 ❍ /rlg: Join ears,nose,mouth and create an emo ;-;
 ❍ /shout <keyword>: write anything you want to give loud shout
 ❍ /weebify <text>: returns a weebified text
 ❍ /sanitize: always use this before /pat or any contact
 ❍ /pat: pats a user, or get patted
 ❍ /8ball: predicts using 8ball method
        """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(fun)")
                 ]
                ]
            ),
        )


def india_fun_emoji_callback(update, context):
    query = update.callback_query
    if query.data == "indiafunemoji_":
        query.message.edit_text(
            text=""" Here is the help for the *Emojis* module:

  ❍ /love ❣️
  ❍ /hack 👨‍💻
  ❍ /bombs 💣
  ❍ /moon 🌚
  ❍ /clock 🕛
  ❍ /earth 🌍
  ❍ /block 🟥
  ❍ /kill ⚰️
  """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(fun)")
                 ]
                ]
            ),
        )


def india_fun_games_callback(update, context):
    query = update.callback_query
    if query.data == "indiafungames_":
        query.message.edit_text(
            text=""" Here is the help for the *Games* module:

  ❍ /game or /games : we have added some games for you.

 Play Game With Emojis:
  ❍ /dice or /dice 1 to 6 any value
  ❍ /ball or /ball 1 to 5 any value
  ❍ /dart or /dart 1 to 6 any value
 Usage: hahaha just a magic.
 warning: you would be in trouble if you input any other value than mentionedinteger X>*:* deletes the replied message, and X messages following it if replied to a message.
              """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(fun)")
                 ]
                ]
            ),
        )



def india_fun_couple_callback(update, context):
    query = update.callback_query
    if query.data == "indiafuncouple_":
        query.message.edit_text(
            text=""" Here is the help for the *Couples* module:

 ❍ /couples - To Choose Couple Of The Day
               """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(fun)")
                 ]
                ]
            ),
        )


def india_fun_karma_callback(update, context):
    query = update.callback_query
    if query.data == "indiafunkarma_":
        query.message.edit_text(
            text=""" Here is the help for the *Karma* module:
 
  Karma point it's point game u can give to ur fellow members in ur group etc 
  Inspired by combot
  Usage : 
  if u wanna give Karma point to for friend u can use some words like
  Pro , thanks you , ty or can use emoji like"👍" or u can use symbols like "+".

  If u wanna decrease someone karma point u can use emoji like 👎 or symbol like "-"

  ❍ /karma:- know ur or something other karma point in ur
  ❍ /karmastat (on/off) :- to enable or disable Karma system in ur group 
 """,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Back", callback_data="help_module(fun)")
                 ]
                ]
            ),
        )






# Handlers start from here 

fun_callback_handler = CallbackQueryHandler(india_fun_callback, pattern=r"indiafun_", run_async=True)
fun_emoji_callback_handler = CallbackQueryHandler(india_fun_emoji_callback, pattern=r"indiafunemoji_", run_async=True)
fun_games_callback_handler = CallbackQueryHandler(india_fun_games_callback, pattern=r"indiafungames_", run_async=True)
fun_couple_callback_handler = CallbackQueryHandler(india_fun_couple_callback, pattern=r"indiafuncouple_", run_async=True)
fun_karma_callback_handler = CallbackQueryHandler(india_fun_karma_callback, pattern=r"indiafunkarma_", run_async=True)






