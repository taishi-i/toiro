import os
import pathlib


base = pathlib.Path(os.path.abspath(__file__))
base = str(base.parent)

sample_train = os.path.join(base, "data", "sample.train")
sample_dev = os.path.join(base, "data", "sample.dev")
sample_test = os.path.join(base, "data", "sample.test")
sample_txt = os.path.join(base, "data", "sample.txt")
