#!/home/charlie/miniconda3/envs/semanticKitti/bin python3

import load_file


def replace_intensity_by_label(points, labels):
    points[:, 3:4] = labels.reshape((-1, 1))
    return points


def save_data(pts, path):
    pts.tofile(path)


scans_paths = load_file.load_bin_path()
labels_paths = load_file.load_label_path()

for i in range(len(scans_paths)):
    scan_file = scans_paths[i]
    label_file = labels_paths[i]
    pt = load_file.load_bin(scan_file)
    semiLabel = load_file.load_label(label_file)
    pt_label = replace_intensity_by_label(pt, semiLabel)
    save_data(pt_label, scan_file)
    print(scan_file)
    print()
