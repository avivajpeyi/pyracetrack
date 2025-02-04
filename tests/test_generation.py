from pyracetrack import Track
from pyracetrack.cli import main
import os
import pytest
import matplotlib.pyplot as plt
from click.testing import CliRunner


HERE = os.path.dirname(__file__)
OUTDIR = os.path.join(HERE, "test_output")
os.makedirs(OUTDIR, exist_ok=True)

@pytest.fixture()
def outdir():
    return OUTDIR



def test_generate_2d(outdir):
    track = Track.generate(seed=0)
    track.plot()
    plt.savefig(os.path.join(outdir, "2d_track.png"))


def test_generate_3d(outdir):
    track = Track.generate(seed=0, track_3d=True)
    track.plot()
    plt.savefig(os.path.join(outdir, "3d_track.png"))


def test_cli():
    runner = CliRunner()
    result = runner.invoke(
        main, ["--3d", "--seed", "0", "--maxx", "100", "--maxy", "100", "--corner_cells", "15", "--noise_factor", "10", "--noise_octaves", "2", "--num_points", "10"]
    )
    assert result.exit_code == 0