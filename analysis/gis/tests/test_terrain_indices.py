"""``analysis.gis.terrain_indices`` のテスト。"""

import pytest

from analysis.gis.terrain_indices import (
    distance_to_stream,
    load_dem,
    slope,
    surrounding_relief,
    topographic_position_index,
    topographic_wetness_index,
)


class TestLoadDem:
    @pytest.fixture
    def target(self):
        return load_dem

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")


class TestSlope:
    @pytest.fixture
    def target(self):
        return slope

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")


class TestTopographicPositionIndex:
    @pytest.fixture
    def target(self):
        return topographic_position_index

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")


class TestTopographicWetnessIndex:
    @pytest.fixture
    def target(self):
        return topographic_wetness_index

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")


class TestDistanceToStream:
    @pytest.fixture
    def target(self):
        return distance_to_stream

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")


class TestSurroundingRelief:
    @pytest.fixture
    def target(self):
        return surrounding_relief

    @pytest.mark.skip(reason="未実装")
    def test_it(self):
        pytest.fail("未実装")
