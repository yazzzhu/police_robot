from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage,ImageSendMessage,StickerSendMessage,LocationSendMessage,QuickReply,QuickReplyButton,MessageAction
#放入處理回覆訊息所需的模組
from linebot.models import TemplateSendMessage,ButtonsTemplate,MessageTemplateAction,URITemplateAction,PostbackTemplateAction
#放入處理按鈕樣板所需的模組
from linebot.models import FlexSendMessage
#放入處理flex message所需的模組

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendQAButton(event):
    try:
        message = FlexSendMessage(
            alt_text = "警政統計問答Q&A",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "aspectRatio": "4:3",
                            "aspectMode": "cover",
                            "size": "full",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png"
                        },
                        {
                            "type": "text",
                            "text": "警政統計問答",
                            "color": "#7878FF",
                            "size": "xl",
                            "weight": "bold",
                            "offsetStart": "lg",
                            "margin": "md"
                        },
                        {
                            "type": "text",
                            "text": "有什麼想問的呢?",
                            "size": "sm",
                            "color": "#808080",
                            "offsetStart": "lg"
                        }
                        ]
                    }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "問題1",
                        "text": "Q001"
                        },
                        "height": "sm",
                        "color": "#B0AEFF",
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "問題2",
                        "text": "Q002"
                        },
                        "height": "sm",
                        "color": "#7878FF",
                        "margin": "xs",
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "問題3",
                        "text": "Q003"
                        },
                        "height": "sm",
                        "color": "#B0AEFF",
                        "style": "primary",
                        "margin": "xs"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "問題4",
                        "text": "Q004"
                        },
                        "height": "sm",
                        "color": "#7878FF",
                        "margin": "xs",
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "問題5",
                        "text": "Q005"
                        },
                        "height": "sm",
                        "color": "#B0AEFF",
                        "style": "primary",
                        "margin": "xs"
                    }
                    ]
                }
                }
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='ERROR!')
        )

def send001(event):
    try:
        message = TextSendMessage(
            text = 'A001',
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='ERROR!')
        )

def send002(event):
    try:
        message = TextSendMessage(
            text = 'A002',
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='ERROR!')
        )

def send003(event):
    try:
        message = TextSendMessage(
            text = 'A003',
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='ERROR!')
        )

def send004(event):
    try:
        message = TextSendMessage(
            text = 'A004',
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='ERROR!')
        )

def send005(event):
    try:
        message = TextSendMessage(
            text = 'A005',
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='ERROR!')
        )
