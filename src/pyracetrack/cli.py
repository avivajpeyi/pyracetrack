import click
from .track import Track

@click.command()
@click.option('--3d', 'track_3d', is_flag=True, default=False, help='Create 3D racetrack or not')
@click.option('--seed', type=int, default=None, help='Specify int32 seed')
@click.option('--maxx', type=int, default=100)
@click.option('--maxy', type=int, default=100)
@click.option('--corner_cells', type=int, default=15)
@click.option('--noise_factor', type=float, default=10)
@click.option('--noise_octaves', type=int, default=2)
@click.option('--num_points', type=int, default=10)
def main(track_3d, seed, maxx, maxy, corner_cells, noise_factor, noise_octaves, num_points):
    track = Track.generate(
        n=num_points,
        x_bounds=[0, maxx],
        y_bounds=[0, maxy],
        corner_cells=corner_cells,
        seed=seed,
        track_3d=track_3d,
        noise_factor=noise_factor,
        noise_octaves=noise_octaves,
    )
    track.plot()

if __name__ == "__main__":
    main()

