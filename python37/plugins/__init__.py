from importlib import import_module
from importlib import resources

PLUGINS = dict()


def register_plugin(func):
    """注册插件的装饰器"""
    name = func.__name__
    PLUGINS[name] = func
    return func


def __getattr__(name):
    """返回对应名称的插件"""
    try:
        return PLUGINS[name]
    except KeyError:
        _import_plugins()
        if name in PLUGINS:
            return PLUGINS["name"]
        else:
            raise AttributeError(
                f"module {__name__!r} has no attribute {name!r}"
            ) from None


def __dir__():
    """返回可用插件列表"""
    _import_plugins()
    return list(PLUGINS.keys())


def _import_plugins():
    """导入所有资源来注册插件"""
    print(__name__)
    for name in resources.contents(__name__):
        if name.endswith(".py"):
            import_module(f"{__name__}.{name[:-3]}")