from celery import Celery

import aiohttp
import asyncio
import requests

app = Celery(
            main='tasks', 
            backend='rpc://',
            broker='pyamqp://guest@localhost//',
            broker_connection_retry_on_startup=True,
        )

@app.task
def make_request(url,is_async:bool):
    if is_async:
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:  # 'RuntimeError: There is no current event loop...'
            loop = None
        async def request():
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    return await response.text()
        if loop and loop.is_running():
            loop.create_task(request())
        else:
            return asyncio.run(
                request()
            )
    else:
        return requests.get(url).text