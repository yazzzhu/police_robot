from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage
from module import func,func2,func3

#from django.http import HttpResponse

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

#def homeview(request):
#    return HttpResponse("Hello django!")

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '主題一':
                        func.sendText1(event)
    
                    elif mtext == '警政統計問答':
                        func2.sendQAButton(event)
    
                    elif mtext == 'Q001':
                        func2.send001(event)
    
                    elif mtext == 'Q002':
                        func2.send002(event)

                    elif mtext == 'Q003':
                        func2.send003(event)

                    elif mtext == 'Q004':
                        func2.send003(event)

                    elif mtext == 'Q005':
                        func2.send003(event)

                    elif mtext == '統計主題圖卡':
                        func3.sendTextFlexImage(event)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
