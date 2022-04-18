import justpy as jp
from webapp import layout


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page!",
               classes="text-4xl m-2")
        jp.Div(a=div, text="""
        This WebApp lets you type an English word and then , when you finish typing it 
        shows you some of it's definitions. So , go to the dictionary tab and check it out!
        """,
               classes="text-lg")
        return wp



