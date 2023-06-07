from typing import Any, Callable, Coroutine, TypeVar
import asyncio


def execute_async_to_sync(func: Callable, *args, **kwargs) -> Any:
    loop = asyncio.new_event_loop()
    return loop.run_until_complete(func(*args, **kwargs))
