import os
import logging
import matplotlib.pyplot as plt
import sys

logging.getLogger().setLevel(logging.INFO)


def visualize_statistics(statistics: dict, visual_directory: str) -> None:
    """
    The function visualize statistics and save the result to some directory

    :param statistics - statistics for visualization
    :param visual_directory - path to directory
    """
    plt.ylabel("Work time, s")
    plt.xlabel("Processes")
    plt.title("Enumeration statistics")
    pools, work_times = statistics.keys(), statistics.values()
    plt.bar(pools, work_times, color="blue", width=0.25)
    try:
        plt.savefig(os.path.join(visual_directory, "statistics.jpg"))
    except OSError as err:
        logging.warning(
            f"Bar chart wasn't saved to the directory {visual_directory}")
        sys.exit(err)
    logging.info(
        f"Bar chart was successfully saved to the directory {visual_directory}")