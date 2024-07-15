"""
PyTorch Lightning DataModule for SALTED dataset
"""

import os
from os.path import exists as pexists
from os.path import join as pjoin
from typing import Any, Dict, Optional, Tuple, Union

import torch
import yaml
from lightning import LightningDataModule
from torch import Tensor
from torch.utils.data import DataLoader, Dataset, random_split


def valid_salted_data_dir(data_dir: str):
    r""" validate the data directory structure

    `data` directory structure:
    ```text
    my_dataset
    ├── qmdata
    │   ├── overlaps
    │   │   ├── overlap_conf[\d+].npy
    │   │   └── ...
    │   ├── coefficients
    │   │   ├── coefficients_conf[\d+].npy
    │   │   └── ...
    │   └── projections
    │       ├── projections_conf[\d+].npy
    │       └── ...
    │
    ├── descriptors  # descriptor for each input geometry
    │   ├── descriptor_conf[\d+].npz  # for each lambda
    │   └── ...
    ├── basis_data.yaml  # about DF basis set
    ├── geoms.xyz
    └── REDME.md
    """
    get_fname_by_type = {
        "overlaps": lambda i: f"overlap_conf{i}.npy",
        "coefficients": lambda i: f"coefficients_conf{i}.npy",
        "projections": lambda i: f"projections_conf{i}.npy",
    }

    # check if subdirs exist
    for subpath in (
        "qmdata",
        "qmdata/overlaps",
        "qmdata/coefficients",
        "qmdata/projections",
        "geoms.xyz",
    ):
        assert pexists(pjoin(data_dir, subpath)), f"missing {subpath} in {data_dir}"
    # check number of files in each subdir
    num_geoms = len(torch.load(pjoin(data_dir, "geoms.xyz")))
    for subdir, get_fname in get_fname_by_type.items():
        data_files = [n for n in os.listdir(pjoin(data_dir, subdir)) if n.endswith(".npy")]
        assert set(data_files) == {get_fname(i) for i in range(1, num_geoms+1)}, f"missing files in {subdir}"


class SALTEDDataModule(LightningDataModule):
    """plain data module without graph data implementation"""
    def __init__(
        self,
        data_dir:str,
        train_val_test_split: Union[Tuple[int, int, int], Tuple[float, float, float]] = (0.8, 0.1, 0.1),
        batch_size:int=16,
        num_workers:int=0,
        pin_memory:bool=False,
    ):
        super().__init__()
        self.save_hyperparameters()
        self.data_dir = data_dir
        valid_salted_data_dir(data_dir)








class SALTEDGraphDataModule(LightningDataModule):
    """ data module with graph data implementation """

