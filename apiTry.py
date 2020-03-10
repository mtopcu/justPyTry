import justpy as jp
from modules.weather import getWeather
from modules.currency import getRate


def weather_click(self, msg):
    self.message.text = getWeather()
    self.message.classes = 'bg-red-500 text-xl my-4'


def rate_click(self, msg):
    self.message.text = getRate()
    self.message.classes = 'bg-blue-500 text-xl my-4'


def event_demo():
    wp = jp.WebPage()
    button_div = jp.Div(classes='flex m-4 flex-wrap', a=wp)
    w_button_classes = 'bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 border border-blue-700 rounded ' \
                       'mr-2 '
    r_button_classes = 'bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 ' \
                       'rounded mr-2 '

    w_message = jp.Div(text='Click ↑ button to get weather condition', classes='text-xl my-4', a=wp)
    r_message = jp.Div(text='Click ↑ button to get currency', classes='text-xl my-4', a=wp)

    bw = jp.Button(text='Weather', a=button_div, classes=w_button_classes, click=weather_click)
    bw.message = w_message

    br = jp.Button(text='Currency', a=button_div, classes=r_button_classes, click=rate_click)
    br.message = r_message
    return wp


jp.justpy(event_demo)
