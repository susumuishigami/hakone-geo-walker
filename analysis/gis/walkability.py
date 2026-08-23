"""歩行容易性スコアと係数逆算のスタブ。

地形指標（勾配・距離・累積上昇＋周囲標高差積分・TPI・TWI・距離 to 水系）を
合成して歩行容易性スコアを定義する。谷筋度・湿潤 proxy の係数は未知のため、
実地歩行ログの結果に対して逆算して推定する。

再現性のため、係数推定では乱数シードを固定し、入力データのパス・バージョンを
明示すること。
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class WalkabilityWeights:
    """歩行容易性スコアの各説明変数に対する係数。"""

    slope: float
    distance: float
    ascent: float
    relief: float  # 周囲標高差積分（谷筋度）
    wetness: float  # 湿潤 proxy（TWI / 距離 to 水系 由来）


def walkability_score(features: dict[str, float], weights: WalkabilityWeights) -> float:
    """地形指標の辞書と係数から歩行容易性スコアを返す。"""
    raise NotImplementedError  # pragma: no cover


def calibrate_weights(
    features_per_segment: list[dict[str, float]],
    observed_effort: list[float],
    seed: int = 0,
) -> WalkabilityWeights:
    """実地ログの主観/客観負担に対し係数を逆算（フィッティング）して返す。

    ``observed_effort`` は区間ごとの実測負担（速度・RPE 等から導出）。
    ``seed`` は再現性のための乱数シード。
    """
    raise NotImplementedError  # pragma: no cover
