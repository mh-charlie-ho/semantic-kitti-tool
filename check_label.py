#!/home/charlie/miniconda3/envs/semanticKitti/bin python3
import load_file as lf
import numpy as np

bin_paths = lf.load_bin_path()
label_paths = lf.load_label_path()
pt_path = bin_paths[0]
label_path = label_paths[0]
pts = lf.load_bin(pt_path)
inst_label, sem_label = lf.load_label(label_path, do_inst=True)

inst_label = inst_label.astype(np.int32)
sem_label = sem_label.astype(np.int32)

inst_label = np.array([inst_label]).T
sem_label = np.array([sem_label]).T

print(inst_label)
print(sem_label)
verification = np.concatenate((inst_label, sem_label), axis=1)

for i in verification:
    # if not i[0] == 0:
    print(i)
