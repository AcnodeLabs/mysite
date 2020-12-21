from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from xal import mykey

bot_configuration = BotConfiguration(
	name='PythonSampleBot',
	avatar='http://viber.com/avatar.jpg',
	auth_token=mykey('viber')
)

viber = Api(bot_configuration)
# users = viber.get_online(['+923212358712','+923215308951'])
# print(users)