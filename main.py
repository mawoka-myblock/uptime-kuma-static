import asyncio
import sys

import socketio
import json
import aiofiles
from jinja2 import Template
from os import getenv

config_login_password_auth = getenv("PASSWORD_LOGIN")
config_password_login_password = getenv("UTKUMA_PASSWORD")
config_password_login_username = getenv("UTKUMA_USERNAME")
config_token_token = getenv("UTKUMA_TOKEN")
config_base_url = getenv("UTKUMA_URL")

sio = socketio.AsyncClient()
mons = []


async def write_template():
    async with aiofiles.open("templates/template.jinja2", "r") as f:
        template = Template(await f.read(), enable_async=True)
    async with aiofiles.open("out/index.html", "w") as f:
        await f.write(await template.render_async(mons=mons))


async def handle_callback(data):
    #print(data)
    pass


async def stop_after_10():
    await sio.sleep(7)
    sys.exit()


@sio.event
async def connect():
    print('connection established')
    if config_login_password_auth:
        await sio.emit("login",
                       {"username": config_password_login_username, "password": config_password_login_password},
                       callback=handle_callback)
    else:
        await sio.emit("loginByToken", config_token_token, callback=handle_callback)


@sio.event
async def monitorList(data):
    for i in data:
        if data[i]["active"] == 1:
            mons.append({"id": data[i]["id"], "name": data[i]["name"], "url": data[i]["url"]})


@sio.event
async def uptime(monitor_id, data, uptime_time):
    if data == 720:
        for i in mons:
            if int(i["id"]) == int(monitor_id):
                i["uptime_percent"] = str(uptime_time * 100)[:5]

    await write_template()


@sio.event
async def heartbeatList(id, data):
    for i in mons:
        if i["id"] == data[0]["monitorID"]:
            try:
                i["uptime"] = data
            except KeyError:
                pass



@sio.event
async def disconnect():
    print('disconnected from server')


async def main():
    task = sio.start_background_task(stop_after_10)
    await sio.connect(config_base_url)
    await sio.wait()


if __name__ == "__main__":
    asyncio.run(main())
