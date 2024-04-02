from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage,ImageSendMessage,StickerSendMessage,LocationSendMessage,QuickReply,QuickReplyButton,MessageAction
#放入處理回覆訊息所需的模組
from linebot.models import FlexSendMessage
#放入處理flex message所需的模組

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

def sendTextFlexImage(event):
    try:
        message = FlexSendMessage(
            alt_text = "警政統計主題圖卡",
            contents={
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "行人路權優先，保障你我安全",
                            "color": "#ffffff",
                            "weight": "bold",
                            "align": "center",
                            "size": "lg"
                        }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://github.com/yazzzhu/police_robot/blob/master/image/1%E4%BA%A4%E9%80%9A.png?raw=true",
                            "size": "full",
                            "align": "center",
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://github.com/yazzzhu/police_robot/blob/master/image/1%E4%BA%A4%E9%80%9A.png?raw=true"
                            }
                        },
                        {
                            "type": "separator"
                        },
                        {
                            "type": "text",
                            "text": "近5年高雄市行人交通事故件數……",
                            "margin": "lg"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "了解更多",
                            "uri": "https://kcpd.kcg.gov.tw/News_Content.aspx?n=EF52D09631BD16DF&sms=891486F7A6BFF569&s=599332A021320E12"
                            }
                        }
                        ]
                    },
                    "styles": {
                        "header": {
                        "backgroundColor": "#B0AEFF"
                        }
                    }
                    },
                    {
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "攜手反暴力 愛擁抱不擁暴",
                            "color": "#ffffff",
                            "size": "lg",
                            "weight": "bold"
                        }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://github.com/yazzzhu/police_robot/blob/master/image/2%E5%AE%B6%E6%9A%B4.png?raw=true",
                            "size": "full",
                            "align": "center",
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://github.com/yazzzhu/police_robot/blob/master/image/2%E5%AE%B6%E6%9A%B4.png?raw=true"
                            }
                        },
                        {
                            "type": "separator"
                        },
                        {
                            "type": "text",
                            "text": "為防治家庭暴力行為與保護被害人權益……",
                            "margin": "lg"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "了解更多",
                            "uri": "https://kcpd.kcg.gov.tw/News_Content.aspx?n=EF52D09631BD16DF&sms=891486F7A6BFF569&s=A13A4E2BA960766E"
                            }
                        }
                        ]
                    },
                    "styles": {
                        "header": {
                        "backgroundColor": "#7878FF"
                        }
                    }
                    },
                    {
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "詐欺花招多，小心謹慎看緊辛苦錢！",
                            "color": "#ffffff",
                            "weight": "bold",
                            "align": "center",
                            "size": "lg"
                        }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://github.com/yazzzhu/police_robot/blob/master/image/3%E8%A9%90%E9%A8%99.png?raw=true",
                            "size": "full",
                            "align": "center",
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://github.com/yazzzhu/police_robot/blob/master/image/3%E8%A9%90%E9%A8%99.png?raw=true"
                            }
                        },
                        {
                            "type": "separator"
                        },
                        {
                            "type": "text",
                            "text": "112年高雄市詐欺案件占全般刑案11.83%……",
                            "margin": "lg"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "了解更多",
                            "uri": "https://kcpd.kcg.gov.tw/News_Content.aspx?n=EF52D09631BD16DF&sms=891486F7A6BFF569&s=51FE6A2309B2325C"
                            }
                        }
                        ]
                    },
                    "styles": {
                        "header": {
                        "backgroundColor": "#B0AEFF"
                        }
                    }
                    },
                    {
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "尋獲失蹤人口撫平家屬擔憂",
                            "color": "#ffffff",
                            "size": "lg",
                            "weight": "bold"
                        }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://github.com/yazzzhu/police_robot/blob/master/image/4%E5%A4%B1%E8%B9%A4.png?raw=true",
                            "size": "full",
                            "align": "center",
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://github.com/yazzzhu/police_robot/blob/master/image/4%E5%A4%B1%E8%B9%A4.png?raw=true"
                            }
                        },
                        {
                            "type": "separator"
                        },
                        {
                            "type": "text",
                            "text": "近5年高雄市每年失蹤人口發生數約介於……",
                            "margin": "lg"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "了解更多",
                            "uri": "https://kcpd.kcg.gov.tw/News_Content.aspx?n=EF52D09631BD16DF&sms=891486F7A6BFF569&s=639D3F27CB77DE1B"
                            }
                        }
                        ]
                    },
                    "styles": {
                        "header": {
                        "backgroundColor": "#7878FF"
                        }
                    }
                    },
                    {
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "落實推動性別平等，營造友善職場：近10年女性警察官占比逐年提升！",
                            "color": "#ffffff",
                            "weight": "bold",
                            "align": "center",
                            "size": "lg"
                        }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://github.com/yazzzhu/police_robot/blob/master/image/5%E8%AD%A6%E5%93%A1%E6%95%B8.png?raw=true",
                            "size": "full",
                            "align": "center",
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://github.com/yazzzhu/police_robot/blob/master/image/5%E8%AD%A6%E5%93%A1%E6%95%B8.png?raw=true"
                            }
                        },
                        {
                            "type": "separator"
                        },
                        {
                            "type": "text",
                            "text": "在性別平等工作持續推動下，近10年……",
                            "margin": "lg"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "了解更多",
                            "uri": "https://kcpd.kcg.gov.tw/News_Content.aspx?n=EF52D09631BD16DF&sms=891486F7A6BFF569&s=0D7095AB0D8EC979"
                            }
                        }
                        ]
                    },
                    "styles": {
                        "header": {
                        "backgroundColor": "#B0AEFF"
                        }
                    }
                    },
                    {
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "民眾生命安全之守護神：近10年治安數據呈「發生數下降、破獲率增加。」持續進步趨勢",
                            "color": "#ffffff",
                            "size": "lg",
                            "weight": "bold"
                        }
                        ]
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://github.com/yazzzhu/police_robot/blob/master/image/6%E5%88%91%E4%BA%8B.png?raw=true",
                            "size": "full",
                            "align": "center",
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://github.com/yazzzhu/police_robot/blob/master/image/6%E5%88%91%E4%BA%8B.png?raw=true"
                            }
                        },
                        {
                            "type": "separator"
                        },
                        {
                            "type": "text",
                            "text": " 近10年高雄市全般刑案發生數呈下降趨勢……",
                            "margin": "lg"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "uri",
                            "label": "了解更多",
                            "uri": "https://kcpd.kcg.gov.tw/News_Content.aspx?n=EF52D09631BD16DF&sms=891486F7A6BFF569&s=147C187738435E92"
                            }
                        }
                        ]
                    },
                    "styles": {
                        "header": {
                        "backgroundColor": "#7878FF"
                        }
                    }
                    }
                ]
            }
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='ERROR!')
        )

