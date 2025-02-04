import numpy as np
import matplotlib.pyplot as plt
from .core import create_loop_points


class Track:
    """
    Represents a racetrack with plotting capabilities.
    """

    def __init__(self, points: np.ndarray, track_3d: bool = False, seed: int = None) -> None:
        self.points = points
        self.track_3d = track_3d
        self.seed = seed

    @classmethod
    def generate(
            cls,
            n: int = 10,
            x_bounds: list = [0, 100],
            y_bounds: list = [0, 100],
            noise_factor: float = 10,
            noise_octaves: int = 2,
            corner_cells: int = 15,
            track_3d: bool = False,
            seed: int = None,
    ) -> "Track":
        """Generates a racetrack using the generate_track_points function."""
        if seed is None:
            seed = np.random.randint(0, 2 ** 32)

        curves, height_map = create_loop_points(n, x_bounds, y_bounds, noise_factor, noise_octaves, corner_cells, seed)
        if track_3d == True:
            points_3d = []
            for i in range(len(curves)):
                x = int(curves[i][0])
                y = int(curves[i][1])
                points_3d.append([curves[i][0], height_map[x][y], curves[i][1]])
            curves = points_3d


        return cls(points=np.array(curves), track_3d=track_3d, seed=seed)

    def plot(
            self,
            ax=None,
            background_color: str = "black",
            line_color: str = "white",
            line_width: float = 2,
            text_color: str = "red",
            show_seed: bool = True,
    ) -> None:
        """Plots the racetrack in 2D or 3D."""

        if self.track_3d:
            if ax is None:
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
            ax.plot(self.points[:, 0], self.points[:, 1], self.points[:, 2],
                    color=line_color, linewidth=line_width)

        else:
            if ax is None:
                fig, ax = plt.subplots()
            ax.plot(self.points[:, 0], self.points[:, 1],
                    color=line_color, linewidth=line_width
                    )

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        if show_seed:
            ax.set_title(f"Seed: {self.seed}", color=text_color)
        ax.set_facecolor(background_color)

