import os
from vkbottle.bot import Bot, Message
from vkbottle_types.objects import UsersUserFull
from vkbottle import BaseMiddleware, CtxStorage


from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("VK_TOKEN")

bot = Bot(token=TOKEN)

redis_gateway = CtxStorage()



class NoBotMiddleware(BaseMiddleware[Message]):
    async def pre(self):
        if self.event.from_id < 0:
            self.stop("Группе не разрешается использовать бота")


class RegistrationMiddleware(BaseMiddleware[Message]):
    call_count = 0

    def __init__(self, event, view):
        super().__init__(event, view)
        self.cached = False

    async def pre(self):
        user = redis_gateway.get(self.event.from_id)
        if user is None:
            user = (await bot.api.users.get(self.event.from_id))[0]
            redis_gateway.set(self.event.from_id, user)
            self.cached = False
        else:
            self.cached = True
        self.send({"info": user})

    async def post(self):
        if who_i_am_handler in self.handlers:
            self.__class__.call_count += 1
            cached_str = "был" if self.cached else "не был"
            await self.event.answer(
                f"Ответ {cached_str} взят из кеша. Количество вызовов: {self.call_count}"
            )

class InfoMiddleware(BaseMiddleware[Message]):
    async def post(self):
        if not self.handlers:
            self.stop("Сообщение не было обработано")

        await self.event.answer(
            "Сообщение было обработано:\n\n"
            f"View - {self.view}\n\n"
            f"Handlers - {self.handlers}"
        )

@bot.on.message(lev="кто я")
async def who_i_am_handler(message: Message, info: UsersUserFull):
    await message.answer(f"Ты - {info.first_name}")

bot.labeler.message_view.register_middleware(NoBotMiddleware)
bot.labeler.message_view.register_middleware(RegistrationMiddleware)
bot.labeler.message_view.register_middleware(InfoMiddleware)


