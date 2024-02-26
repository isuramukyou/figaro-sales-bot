from environs import Env

env = Env()
env.read_env()

BOT_TOKEN: str = env.str('BOT_TOKEN')
API_HOST: str = env.str('API_HOST')
API_USERNAME: str = env.str('API_USERNAME')
API_PASSWORD: str = env.str('API_PASSWORD')
