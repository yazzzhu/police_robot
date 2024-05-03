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
                        "type": "image",
                        "aspectRatio": "4:3",
                        "aspectMode": "cover",
                        "size": "full",
                        "url": "https://github.com/yazzzhu/police_robot/blob/master/image/line_QA%E5%9C%96_QA_%E5%B7%A5%E4%BD%9C%E5%8D%80%E5%9F%9F%201.png?raw=true"
                    },
                    {
                        "type": "text",
                        "text": "警政統計問答",
                        "color": "#B09FFF",
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
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "① 關於 主題1 ０１２３４５６７８",
                        "text": "Q001"
                        },
                        "color": "#8589c0",
                        "style": "link"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "② 關於 主題2",
                        "text": "Q002"
                        },
                        "color": "#8589c0",
                        "style": "link"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "③ 關於 主題3",
                        "text": "Q003"
                        },
                        "color": "#8589c0",
                        "style": "link"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "④ 關於 主題4",
                        "text": "Q004"
                        },
                        "color": "#8589c0",
                        "style": "link"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "⑤ 關於 主題5",
                        "text": "Q005"
                        },
                        "color": "#8589c0",
                        "style": "link"
                    }
                    ],
                    "alignItems": "flex-start",
                    "position": "relative",
                    "paddingTop": "sm",
                    "paddingBottom": "lg",
                    "paddingStart": "xl",
                    "paddingEnd": "xl"
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
