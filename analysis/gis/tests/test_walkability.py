"""``analysis.gis.walkability`` のテスト。"""

import pytest

from analysis.gis.walkability import calibrate_weights, walkability_score


class TestWalkabilityScore:
    @pytest.fixture
    def target(self):
        return walkability_score

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")


class TestCalibrateWeights:
    @pytest.fixture
    def target(self):
        return calibrate_weights

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")
