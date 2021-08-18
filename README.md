# A Hybrid Neural Network Approach for Increasing the Absolute Accuracy of Industrial Robots

This repository contains a dataset of real robot measurements for robot accuracy improvement.

Detailed description of the dataset composition and procedure is available in our [paper](https://emse.fr/~garaix/detailprg/CASE21_ContentListMedia_2.html#tubt2_06).

## Dataset description

Each series consists of three files:
- A file containing the obtained pairs of commanded pose and actual, measured pose, the joint configuration a timestamp and the environment temperature.
- An individual measurement file, which can be used for extrinsic, hand-eye calibration.
- An initial transformation from T-Mac to flange since the path planning and commanded poses are planned regarding T-Mac tcp (to ensure visibility)

Additionally, we provide the following:
- A small python script containint a dataset class for reading and processing the data
- A [video](TODO) which shows the measurement procedure

## Publication

Please cite our work if you use the dataset:

> Landgraf, C., Ernst, K., Schleth, G., Fabritius, M., & Huber, M. F. (2021). A Hybrid Neural Network Approach for Increasing the Absolute Accuracy of Industrial Robots. In 2021 IEEE 17th International Conference on Automation Science and Engineering (CASE) (pp. xx-xx). IEEE.

```
@inproceedings{landgraf2021accuracy,
  title={A Hybrid Neural Network Approach for Increasing the Absolute Accuracy of Industrial Robots},
  author={Landgraf, Christian and Ernst, Kilian and Schleth, Gesine and Fabritius, Marc and Huber, Marco F},
  journal={2021 IEEE 17th International Conference on Automation Science and Engineering (CASE)},
  pages={1138--1144},
  year={2021},
  organization={IEEE},
  address={Lyon, France}
}
```
