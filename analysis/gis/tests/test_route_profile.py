"""``analysis.gis.route_profile`` のテスト。"""

import pytest

from analysis.gis.route_profile import cumulative_ascent, integrate_relief, path_length


class TestCumulativeAscent:
    @pytest.fixture
    def target(self):
        return cumulative_ascent

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")


class TestPathLength:
    @pytest.fixture
    def target(self):
        return path_length

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")


class TestIntegrateRelief:
    @pytest.fixture
    def target(self):
        return integrate_relief

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")
