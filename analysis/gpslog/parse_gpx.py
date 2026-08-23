"""GPX 歩行ログの読み込みスタブ。

GPX パーサ（gpxpy 等）はまだ pyproject に含めていない。本格実装に着手する際、
ユーザー承認のうえ追加する。スタブ段階では標準ライブラリのみに依存する。
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TrackPoint:
    """GPS トラックの 1 点。時刻は UNIX 秒、標高は[m]。"""

    lon: float
    lat: float
    elevation: float
    time: float


def load_track(path: Path) -> list[TrackPoint]:
    """GPX ファイルからトラック点列を読み込んで返す。"""
    raise NotImplementedError  # pragma: no cover
