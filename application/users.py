from vibora import Request
from vibora.blueprints import Blueprint
from vibora.responses import JsonResponse

from application.constants import Methods

users_bp = Blueprint()


@users_bp.route('/', methods=['GET', 'POST'])
async def home(request: Request):
    if request.method == Methods.GET.value:
        return JsonResponse({'hello': 'world'})
    elif request.method == Methods.POST.value:
        return JsonResponse({'teste': 'teste'})
    else:
        raise Exception


@users_bp.route('/exception', methods=['GET'])
async def exception():
    raise Exception('oi')
