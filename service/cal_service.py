class ShopService:
    @staticmethod
    def parse_shop(shop_input: str) -> tuple:
        shop_param = shop_input.split(' ')
        shop_location = {
            # input x, y is not zero based
            'x': int(shop_param[0]) - 1,
            'y': int(shop_param[1]) - 1
        }
        shop_distance = int(shop_param[2])

        return shop_location, shop_distance

    @staticmethod
    def cal_shop_in_map(shop_list: list, _map: list):
        for shop in shop_list:
            location, distance = ShopService.parse_shop(shop)
            ShopService._cal_shop_range(location=location, distance=distance, _map=_map)

        max_in_map = max([max(v) for v in _map])
        # for m in _map:
        #     print(m)
        print(max_in_map)

    @staticmethod
    def _cal_shop_range(location: dict, distance: int, _map: list):
        x = location.get('x', 0)
        y = location.get('y', 0)
        visited = dict()
        ShopService._dfs(x=x, y=y, level=distance + 1, _map=_map, visited=visited)
        print(visited)

    @staticmethod
    def _dfs(x: int, y: int, level: int, _map: list, visited: dict):
        key = "{}-{}".format(x, y)
        if level <= 0 or x < 0 or y < 0 or x > len(_map) - 1 or y > len(_map) - 1 or visited.get(key):
            return None

        _map[x][y] = _map[x][y] + 1

        visited[key] = True

        ShopService._dfs(x + 1, y, level - 1, _map, visited)
        ShopService._dfs(x - 1, y, level - 1, _map, visited)
        ShopService._dfs(x, y + 1, level - 1, _map, visited)
        ShopService._dfs(x, y - 1, level - 1, _map, visited)
