"""バージョンの採番規約と、設定ファイル間の整合のテスト。"""

import pathlib
import re
import runpy
import tomllib

import pytest

# CalVer vYY.MM.N（例: 26.8.1 = 2026年8月の1本目）。連番は1始まり。
CALVER = re.compile(r"^\d{2}\.([1-9]|1[0-2])\.[1-9]\d*$")

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent


class TestProjectVersion:
    @pytest.fixture
    def target(self):
        pyproject = REPO_ROOT / "pyproject.toml"
        data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
        return data["project"]["version"]

    def test_matches_calver(self, target):
        assert CALVER.match(target), f"{target!r} は CalVer YY.MM.N に合致しない"

    def test_matches_sphinx_release(self, target):
        config = runpy.run_path(str(REPO_ROOT / "docs" / "conf.py"))
        assert config["release"] == target
