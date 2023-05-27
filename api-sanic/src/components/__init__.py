from sanic import Sanic
from mangum import Mangum
from constants import setting

print(setting)
app = Sanic("TEST")

handler = Mangum(app)