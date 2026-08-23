"""``analysis.gpslog.segment`` のテスト。"""

import pytest

from analysis.gpslog.segment import WalkSegment, extract_walking_segments


class TestMeanSpeed:
    @pytest.fixture
    def target(self):
        return WalkSegment

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")


class TestExtractWalkingSegments:
    @pytest.fixture
    def target(self):
        return extract_walking_segments

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")
