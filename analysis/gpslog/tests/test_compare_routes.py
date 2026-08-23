"""``analysis.gpslog.compare_routes`` のテスト。"""

import pytest

from analysis.gpslog.compare_routes import compare, summarize_route


class TestSummarizeRoute:
    @pytest.fixture
    def target(self):
        return summarize_route

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")


class TestCompare:
    @pytest.fixture
    def target(self):
        return compare

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")
