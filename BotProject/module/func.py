from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage,ImageSendMessage,StickerSendMessage,LocationSendMessage,QuickReply,QuickReplyButton,MessageAction
#放入處理回覆訊息所需的模組

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendText1(event):
    try:
        message = TextSendMessage(
            text='1111',
        )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='ERROR!')
        )

def sendText2(event):
    try:
        message = TextSendMessage(
            text='2222',
        )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='ERROR!')
        )

def sendText3(event):
    try:
        message = TextSendMessage(
            text='3333',
        )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='ERROR!')
        )

