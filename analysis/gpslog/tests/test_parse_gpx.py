"""``analysis.gpslog.parse_gpx`` のテスト。"""

import pytest

from analysis.gpslog.parse_gpx import load_track


class TestLoadTrack:
    @pytest.fixture
    def target(self):
        return load_track

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")
