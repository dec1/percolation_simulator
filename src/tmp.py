from src._experiment import Experiment
from typing import List
import time
from src._grid_visual import visualize_as_histogram

from dataclasses import dataclass


# --------------------------------------------
@dataclass
class PercResult:
    """Encapsulates all data in calculation"""

    # in:
    num_cols: float
    num_rows: float
    batch_size: int

    # out:
    ps: List[float]  # p-values
    p_av: float  # average p-value
    time_delta: float  # num of secs required to perform calculation


# --------------------------------------------
def calculate_p_av(
    num_rows: int = 30, num_cols: int = 30, batch_size: int = 300, want_vis_clusters=False
) -> PercResult:
    """
    :return:            PercResult with ps, p_av, time_delta calculated


    :param num_rows:    height of grid
    :param num_cols:    width of grid
    :param batch_size:  num of individual values of p used to calculate average
    """

    t0 = time.time()

    ps: List[float] = []
    for i in range(batch_size):
        p_i = Experiment().do_it(num_rows=num_rows, num_cols=num_cols, want_vis_clusters=want_vis_clusters)
        ps.append(float(p_i))

    p_av = sum(ps) / float(len(ps))
    t1 = time.time()

    time_delta = t1 - t0

    result = PercResult(
        num_rows=num_rows, num_cols=num_cols, batch_size=batch_size, ps=ps, p_av=p_av, time_delta=round(time_delta, 2)
    )
    return result


# ------------------------------------------------------------------
file_path = "/Users/declan/Documents/zone/high/text/info/tmp.txt"
if __name__ == "__main__":
    import re

    declan = 3449.60
    irina = 3184.34

    combined = declan + irina
    half = combined / 2.0
    declan_owe = half - declan
    irina_owe = half - irina
    print(f"declan_owe = {declan_owe}, irina_owe = {irina_owe}")

    entries = []
    current_entry = []
    total = 0.0

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                if line in current_entry:
                    continue
                if line == "Kartenzahlung":
                    continue
                current_entry.append(line)
            else:
                if current_entry:
                    entries.append(current_entry)
                    match = re.search(r'\s*-\s*-(\d+[.,]\d+)', '\n'.join(current_entry))
                    if match:
                        # print(f"found match: {match.group(1)}")
                        total += float(match.group(1).replace(',', '.'))
                    # else:
                    # print(f"no match on current_entry: {current_entry}")
                    current_entry = []

    for entry in entries:
        print('\n'.join(entry) + '\n')

    print(f"\ntotal = {total}")
