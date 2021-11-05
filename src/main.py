
class MyClass:
    async def do_inside_class(self):
        return "original"

async def do_class():
    d = MyClass()
    return await d.do_inside_class()


async def do_func():
    return await func_itself()

async def func_itself():
    return "original"