"""2 ルートの歩行ログ比較のスタブ。

湯坂路と箱根八里の歩行セグメントを比較し、速度・所要時間・停止回数などの
要約統計を算出する。両ルートは取得条件（時期・気象・荷重・装備・休憩・GPS 条件・
区間）が異なりうるため、結果は探索・解釈のための資料として扱い、取得条件を併記する。
"""

from dataclasses import dataclass

from analysis.gpslog.segment import WalkSegment


@dataclass(frozen=True)
class RouteSummary:
    """1 ルート分の歩行ログ要約。"""

    name: str
    total_distance_m: float
    total_walking_time_s: float
    mean_speed: float
    stop_count: int


def summarize_route(name: str, segments: list[WalkSegment]) -> RouteSummary:
    """歩行セグメント列から 1 ルート分の要約統計を返す。"""
    raise NotImplementedError  # pragma: no cover


def compare(yuzaka: RouteSummary, hakone_hachiri: RouteSummary) -> dict[str, float]:
    """2 ルートの要約を比較し、差分（速度比など）を返す。"""
    raise NotImplementedError  # pragma: no cover
