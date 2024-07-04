#!/home/charlie/miniconda3/envs/semanticKitti/bin python3
import load_file as lf
import numpy as np
import math


def isInRange(angle, upperDeg=50, lowerDeg=-50):
    return np.deg2rad(lowerDeg) <= angle <= np.deg2rad(upperDeg)


def azimuth_filter(points, labels):
    proPoint = []
    proLabel = []
    # pt: [x, y, z, intensity]
    for point, label in zip(points, labels):
        ang = math.atan2(point[1], point[0])
        if isInRange(ang):
            proPoint.append(point)
            proLabel.append(label)
    return np.array(proPoint), np.array(proLabel)


def save_data(pts, path):
    pts.tofile(path)


bin_paths = lf.load_bin_path()
label_paths = lf.load_label_path()
for i in range(len(bin_paths)):
    pt_path = bin_paths[i]
    label_path = label_paths[i]
    pts = lf.load_bin(pt_path)
    inst_label, sem_label = lf.load_label(label_path, do_inst=True)

    labels = (inst_label << 16) + sem_label
    pts, labels = azimuth_filter(pts, labels)

    pts = pts.astype(np.float32)
    labels = labels.astype(np.uint32)

    save_data(pts, pt_path)
    save_data(labels, label_path)
    print(pt_path)
