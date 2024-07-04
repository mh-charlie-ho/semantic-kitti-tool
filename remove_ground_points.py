#!/home/charlie/miniconda3/envs/semanticKitti/bin python3
import load_file as lf
import numpy as np

ground_point_label = [40]  # the label is only 40.


def remove_points(point, ins_label, sem_label):
    global ground_point_label
    checkedList = np.full(len(sem_label), False, dtype=bool)
    for n in ground_point_label:
        checkedList = checkedList | (sem_label == n)

    label = (ins_label << 16) + ins_label
    true_indices = np.where(checkedList == 1)
    return np.delete(point, true_indices,
                     axis=0), np.delete(label, true_indices)


def save_data(pts, path):
    pts.tofile(path)


bin_paths = lf.load_bin_path()
label_paths = lf.load_label_path()
for i in range(len(bin_paths)):
    pt_path = bin_paths[i]
    label_path = label_paths[i]
    pt = lf.load_bin(pt_path)
    ins, sem = lf.load_label(label_path, do_inst=True)

    new_pt, new_label = remove_points(pt, ins, sem)

    new_pt = new_pt.astype(np.float32)
    new_label = new_label.astype(np.uint32)

    save_data(new_pt, pt_path)
    save_data(new_label, label_path)
    print(pt_path)
