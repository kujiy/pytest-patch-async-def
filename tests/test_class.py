from unittest import mock
from unittest.mock import AsyncMock

import pytest
from src.main import do_class

@pytest.mark.asyncio
@mock.patch('src.main.do_class', new_callable=AsyncMock)
async def test_stuff(mock_duo):
    # code
    mock_duo.return_value="mocked"
    a = await do_class()
    assert a == "mocked"
