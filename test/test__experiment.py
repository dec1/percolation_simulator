""" Experiment tests """

from src._experiment import Experiment

# --------------------------------------------
def test_experiment():
    """ Run an experiment """
    import time

    t0 = time.time()

    num_rows=5
    num_cols=4
    p = Experiment().do_it(num_rows=num_rows, num_cols=num_cols)
    assert 0 <p < 1


    t1 = time.time()

    time_delta = t1 - t0
    print(f"...{round(time_delta,2)} secs for ({num_rows}x{num_cols}) grid")

# --------------------------------------------
