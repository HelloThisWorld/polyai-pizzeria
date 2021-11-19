from service.cal_service import ShopService
from service.param_constant import *


class ParamService:
    @staticmethod
    def resolve_params(params: list):
        map_param = params[0].split(' ')
        shop_param_list = params[1:]

        resolved_params = dict()
        if len(map_param) > 2:
            print('input param error at line 1, expected 2 actual is ', len(map_param))
        else:
            map_size = int(map_param[0])
            matrix = []
            for i in range(map_size):
                row = []
                for j in range(map_size):
                    row.append(0)
                matrix.append(row)

            resolved_params[MAP] = matrix
            resolved_params[SHOP_LIST] = shop_param_list

        ShopService.cal_shop_in_map(shop_list=resolved_params.get(SHOP_LIST), _map=resolved_params.get(MAP))

