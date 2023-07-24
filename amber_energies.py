from pathlib import Path
import re
import numpy as np

#hierarchy: machine > replicate > series > item

data_series_list = ['Etot', 'EKinetic', 'E_vdw', 'E_el', 'E_hbon', 'E_bon', 'E_angle', 'E_dih']

mden_dir = Path("./data/").resolve()

mden_array = []

for mden_path in mden_dir.iterdir():
    if not mden_path.resolve().is_file():
        continue

    with open(mden_path) as f:
        mden_string = f.read().replace("\n", " ")

    mden_list = [[re.sub("L.", "", mden_element) for mden_element in mden_group.split() if re.sub("L.", "", mden_element)] for mden_group in mden_string.split("L0") if mden_group]

    mden_dict = {mden_element: mden_list[0].index(mden_element) for mden_element in mden_list[0]}
    #determine indices
    # indices = [int(mden_dict[data_series]) for data_series in data_series_list]
    #retrieve data
    for data_series in data_series_list:
        mden_array.append([mden_path.stem.split("_")[0], mden_path.stem.split("_")[1],mden_list[0][mden_dict[data_series]], mden_list[:][mden_dict[data_series]]])

print(mden_array)