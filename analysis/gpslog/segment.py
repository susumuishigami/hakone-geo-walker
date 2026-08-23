"""歩行セグメント抽出のスタブ。

信号待ち・撮影・休憩などの停止区間を除外し、連続して歩いている
「歩行セグメント」を切り出す。速度比較の前処理。
"""

from dataclasses import dataclass

from analysis.gpslog.parse_gpx import TrackPoint


@dataclass(frozen=True)
class WalkSegment:
    """連続歩行区間。停止を除外済み。"""

    points: list[TrackPoint]
    distance_m: float
    duration_s: float

    @property
    def mean_speed(self) -> float:
        """平均歩行速度[m/s]。"""
        raise NotImplementedError  # pragma: no cover


def extract_walking_segments(
    track: list[TrackPoint],
    stop_speed_threshold: float = 0.3,
    min_stop_duration_s: float = 30.0,
) -> list[WalkSegment]:
    """トラックから停止を除外して歩行セグメント列を返す。

    ``stop_speed_threshold`` 未満が ``min_stop_duration_s`` 以上続く区間を停止とみなす。
    """
    raise NotImplementedError  # pragma: no cover
