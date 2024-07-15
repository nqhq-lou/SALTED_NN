"""
Precalculate the salted descriptor for each geometries in the dataset
"""

import argparse

from src.utils.mpi import distribute_work, load_mpi, load_print_func


def cal_descriptor():
    dcpt = {l: None for l in range(0, 6)}
    return dcpt

def main():
    """load descriptor settings"""

    """distribute work"""

    """calculate foundation descriptor"""

    """calculate lamda-descriptor"""

    """save descriptors"""

if __name__ == "__main__":
    args = argparse.ArgumentParser(description="Generate SALTED descriptor")
    args.add_argument("--input", "-i", type=str, required=True, help="input geometry data file")
    args.add_argument("--config", "-c", type=str, required=True, help="config file for descriptor")
    args.add_argument("--output", "-o", type=str, required=True, help="output data directory")

