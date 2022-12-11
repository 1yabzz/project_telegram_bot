import unittest
from unittest.mock import AsyncMock

import bot

class MyTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_something(self):
        message = AsyncMock()
        await bot.command_start(message)
        message.answer.assrt_called_with(text = "dxxc")
        print('cocat')

if __name__=='__main__':
    unittest.main