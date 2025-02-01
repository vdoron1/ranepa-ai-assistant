import os
from vkbottle.bot import Bot, Message
from vkbottle import BaseMiddleware, CtxStorage


from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("VK_TOKEN")
bot = Bot(token=TOKEN)

redis_gateway = CtxStorage()


class RegistrationMiddleware(BaseMiddleware[Message]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.event = kwargs.get('event') 
        self.view = kwargs.get('view') 
        
    async def pre(self):
        user = redis_gateway.get(self.event.from_id)

        if user is None:
            user = (await bot.api.users.get(self.event.from_id))[0]
            redis_gateway.set(self.event.from_id, user)
            self.cached = False
        else:
            self.cached = True
        self.send({"info": user})

        redis_gateway.set(self.event.from_id, user)

            
            
bot.labeler.message_view.register_middleware(RegistrationMiddleware)


