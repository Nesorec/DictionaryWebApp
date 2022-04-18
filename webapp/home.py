import justpy as jp
from webapp import layout


class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the home page!",
               classes="text-4xl m-2")
        jp.Div(a=div, text="""
                This page just exists to navigate you through the WebApp and to demonstrate how you can move through 
                multiple WebPages. To learn more about this WebApp , go to the about page please!
                """,
               classes="text-lg")
        return wp


