from openenv.core.env_server.http_server import create_app
from env import RetailAssistantEnv

app = create_app(RetailAssistantEnv)
