from unittest import mock

from unittest.mock import AsyncMock

import pytest
from src.main import do_func

@pytest.mark.asyncio
@mock.patch('src.main.do_func', new_callable=AsyncMock)
async def test_stuff2(mock_do_func):
    # code
    mock_do_func.return_value="mocked"
    a = await do_func()
    assert a == "mocked"

