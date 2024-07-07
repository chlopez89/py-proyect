import store
# from fastapi import FastApi
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact',response_class=HTMLResponse)
async def get_list():
    return """
        <html>
            <head>
                <title>FastAPI - Christian</title>
            </head>
            <body>
                <h1>Datos de contacto</h1>
                <h2> Numero de contaco - 43432343298742 </h2>
            </body>
        </html>
        """


def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()