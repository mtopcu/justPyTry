import justpy as jp

def rot_img():
    wp = jp.WebPage()
    image = jp.Img(src='https://i.ibb.co/Pjh1cJ6/caveman.jpg', a=wp)
    image.classes = 'm-4 p-4 inline-block border border-blue-500 rounded'
    image.style = f'transform: rotate(0deg)'
    image.height = 400
    image.width = 400
    button_div = jp.Div(classes='flex m-4 flex-wrap', a=wp)
    button_classes = 'bg-blue-500 hover:bg-blue-700 text-white py-1 px-2 border border-blue-700 rounded items-center'

    def rotate(self, msg):
        if self.image.style == f'transform: rotate(0deg)':
            self.image.style = f'transform: rotate(90deg)'
        elif self.image.style == f'transform: rotate(90deg)':
            self.image.style = f'transform: rotate(180deg)'
        elif self.image.style == f'transform: rotate(180deg)':
            self.image.style = f'transform: rotate(270deg)'
        elif self.image.style == f'transform: rotate(270deg)':
            self.image.style = f'transform: rotate(0deg)'

    br = jp.Button(text='Rotate', a=button_div, classes=button_classes, click=rotate)
    br.image = image
    return wp

jp.justpy(rot_img)
