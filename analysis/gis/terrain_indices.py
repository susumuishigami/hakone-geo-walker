"""DEM から地形指標を算出するスタブ。

本研究で歩行容易性スコアに用いる地形指標を定義する。実装は今後追加する。

依存ライブラリ（numpy / rasterio など）はまだ pyproject に含めていない。
本格実装に着手する際、ユーザー承認のうえ追加する（サプライチェーン対策）。
そのためスタブ段階では DEM をプレーンな ``list[list[float]]`` で表現する。

座標系・解像度（EPSG コード）は呼び出し側で明示し、混在させないこと。
"""

from pathlib import Path

# 2 次元の標高グリッド（行優先）。本格実装では numpy 配列に置き換える。
Grid = list[list[float]]


def load_dem(path: Path) -> Grid:
    """DEM ファイルを読み込み標高グリッドを返す。"""
    raise NotImplementedError  # pragma: no cover


def slope(dem: Grid, cell_size: float) -> Grid:
    """各セルの勾配（度またはラジアン）を返す。``cell_size`` は地上解像度[m]。"""
    raise NotImplementedError  # pragma: no cover


def topographic_position_index(dem: Grid, radius: int) -> Grid:
    """TPI を返す。正値は尾根、負値は谷を示す。``radius`` は近傍窓の半径[セル]。"""
    raise NotImplementedError  # pragma: no cover


def topographic_wetness_index(dem: Grid, cell_size: float) -> Grid:
    """TWI（地形湿潤指数）を返す。路面の湿りやすさの proxy。"""
    raise NotImplementedError  # pragma: no cover


def distance_to_stream(dem: Grid, cell_size: float, threshold: float) -> Grid:
    """各セルから最寄り水系までの距離[m]を返す。

    ``threshold`` は流路抽出に用いる集水面積のしきい値。
    """
    raise NotImplementedError  # pragma: no cover


def surrounding_relief(dem: Grid, radius: int) -> Grid:
    """各セルの周囲標高差（谷筋度）を返す。

    周囲（``radius`` セル窓）に対する相対的な低さ/高さを定量化する。
    経路に沿って積分した値を歩行容易性の説明変数に加える。
    """
    raise NotImplementedError  # pragma: no cover
