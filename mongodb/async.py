import asyncio

import motor.motor_asyncio


async def get_server_info():
    conn_str = "mongodb+srv://<username>:<password>@<host>/<database>?retryWrites=true&w=majority"
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=100000)
    try:
        print(await client.server_info())
    except Exception:
        print("unable to connect to the server.")

loop = asyncio.get_event_loop() 
loop.run_until_complete(get_server_info())
