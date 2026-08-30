"""経路に沿った地形プロファイルを算出するスタブ。

DEM 由来の指標を経路上のサンプル点に割り当て、距離・累積上昇などを求める。
"""

# (経度, 緯度) または投影座標 (x, y) のサンプル点列。座標系は呼び出し側で明示する。
Point = tuple[float, float]
Route = list[Point]


def cumulative_ascent(elevations: list[float]) -> float:
    """標高列から累積上昇[m]を返す。"""
    raise NotImplementedError  # pragma: no cover


def path_length(route: Route) -> float:
    """経路の総延長[m]を返す。"""
    raise NotImplementedError  # pragma: no cover
