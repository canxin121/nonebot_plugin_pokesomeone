from typing import Annotated

from nonebot import logger
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, MessageEvent, MessageSegment
from nonebot.matcher import Matcher
from nonebot.params import CommandArg, CommandStart, Arg
from nonebot.plugin import PluginMetadata
from nonebot.typing import T_State

from .config import config

__plugin_meta__ = PluginMetadata(
    name="指定戳一戳",
    description="指定戳某人若干次",
    usage="使用 /戳一戳 获取帮助界面",
    extra={},
    supported_adapters=[
        "nonebot.adapters.onebot.v11",
    ],
    type="application",
    homepage="https://github.com/canxin121/nonebot_plugin_pokesome",
)

poke_some = on_command("戳", aliases={"poke"})


@poke_some.handle()
async def _(matcher: Matcher, event: MessageEvent, state: T_State, foo: Annotated[str, CommandStart()],
            args: Message = CommandArg()):
    if (str(event.user_id) in config.po_black_list) or (hasattr(event, "group_id") and str(
            event.group_id) in config.po_black_list):
        logger.info("此qq或qun不可使用戳一戳,跳过")
        await matcher.finish()
    state["cmd_start"] = str(foo)
    for arg in args:
        if arg.type == "at":
            matcher.set_arg("_to", arg.data["qq"])
        elif arg.type == "text":
            if "@" in arg.data["text"]:
                await matcher.finish(f"正确使用方法是 '{str(foo)}戳 @某人 n(次)',@不能只是文本哦")
            else:
                times = str(arg).replace(" ", "").replace("次", "")
                if times.isdigit():
                    matcher.set_arg("times", times)


@poke_some.got("_to", "戳谁啊,@一下,还有你要戳几次啊")
async def _(matcher: Matcher, event: MessageEvent, state: T_State, args: Message = Arg("_to")):
    cmd_start = state["cmd_start"]
    if isinstance(args, list):
        for arg in args:
            if arg.type == "at":
                state["_to"] = arg.data["qq"]
            elif arg.type == "text":
                if "@" in arg.data["text"]:
                    await matcher.finish(f"正确使用方法是 '{cmd_start}戳 @某人 n(次)',@不能只是文本哦")
                else:
                    times = str(arg).replace(" ", "").replace("次", "")
                    if times.isdigit():
                        matcher.set_arg("times", times)
            else:
                await matcher.finish(f"正确使用方法是 '{cmd_start}戳 @某人 n(次)'哦")
    elif isinstance(args, str):
        if args.isdigit():
            state["_to"] = args


@poke_some.got("times", "你要戳几次啊")
async def _(matcher: Matcher, event: MessageEvent, state: T_State, args: Message = Arg("times")):
    cmd_start = state["cmd_start"]
    times = str(args).replace("次", "")
    if times.isdigit():
        times = int(times)
    else:
        await matcher.finish(f"正确使用方法是 '{cmd_start}戳 @某人 n(次)'哦")
    if times > config.po_max:
        await matcher.send(f"最多只能戳{config.po_max}次哦")
        times = config.po_max
    if state["_to"] in config.po_black_list:
        await matcher.finish("不能戳这个人哦")
    while times > 0:
        await matcher.send(Message([
            MessageSegment("poke", {"qq": state["_to"]})]))
        times -= 1
