from fastapi import FastAPI, Response
import uvicorn
from os import system
from urllib.request import urlopen

app = FastAPI()

# General
@app.get("/general/WakeUp") # пробуждение сервера
async def WakeUp():
    system("wakeonlan -i 192.168.31.169 -p 4343 D8:F3:BC:80:FE:E1")
    return "Succesfully!"
@app.get("/general/Reboot") # перезапуск сервера # не работает
async def Reboot():
    system("ssh Maks@192.168.31.169 -p 5291 reboot")
    return "NN rebooting"

# Нейронки

# @app.get("/nn/Focoos")  # запуск фокуса # вроде работает
# async def Focoos():
#     system("python3 /home/maks/Fooocus/webui.py")
#     return "Succesfully!"

@app.get("/nn/automatic/status") # запуск automatic # вроде работает
async def status_automatic():
    url = "http://192.168.31.169:8000/nn/automatic/status"
    response = Response(content=urlopen(url).read())
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

@app.get("/nn/automatic/start") # запуск automatic # вроде работает
async def start_automatic():
    url = "http://192.168.31.169:8000/nn/automatic/start"
    response = Response(content=urlopen(url).read())
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

@app.get("/nn/automatic/kill") # запуск automatic # вроде работает
async def kill_automatic():
    url = "http://192.168.31.169:8000/nn/automatic/kill"
    response = Response(content=urlopen(url).read())
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

# Климат # не работает

@app.get("/air/condition") # сделать замер # не работает
async def current_condition():
    pass

@app.get("air/recentCondition") # последние несколько замеров # не работает
async def recentCondition():
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


