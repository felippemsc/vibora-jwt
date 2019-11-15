from vibora import Vibora
from vibora.responses import JsonResponse

from application.users import users_bp

app = Vibora()
app.add_blueprint(users_bp, prefixes={'users': '/users'})


@app.route('/', methods=['GET'])
async def home():
    return JsonResponse({'a': 1})


@app.handle(Exception)
async def handle_exception():
    return JsonResponse({'msg': 'Exception caught correctly.'})
