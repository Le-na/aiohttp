import aiohttp


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def fetch_safe(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            return await resp.json()


async def fetch_timeout(url):
    async with aiohttp.ClientSession() as session:
        timeout = aiohttp.ClientTimeout(total=2)
        async with session.get(url, timeout=timeout) as resp:
            return await resp.json()