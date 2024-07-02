#!/home/charlie/miniconda3/envs/semanticKitti/bin python3

import os
import numpy as np


def load_bin_path(
    dir="/media/charlie/DataSet/SemanticKitti/use/dataset/sequences/00/velodyne"
):
    scan_paths = dir
    scan_names = [
        os.path.join(dp, f)
        for dp, dn, fn in os.walk(os.path.expanduser(scan_paths)) for f in fn
    ]
    scan_names.sort()
    return scan_names


def load_label_path(
    dir="/media/charlie/DataSet/SemanticKitti/use/dataset/sequences/00/labels"
):
    label_paths = dir
    label_names = [
        os.path.join(dp, f)
        for dp, dn, fn in os.walk(os.path.expanduser(label_paths)) for f in fn
    ]
    label_names.sort()
    return label_names


def load_bin(path):
    scan = np.fromfile(path, dtype=np.float32)
    scan = scan.reshape((-1, 4))
    return scan


def load_label(path):
    label = np.fromfile(path, dtype=np.uint32)
    label = label.reshape((-1))

    sem_label = label & 0xFFFF  # semantic label in lower half
    inst_label = label >> 16  # instance id in upper half
    return sem_label.astype(np.float32)
