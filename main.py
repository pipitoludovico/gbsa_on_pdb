import sys

from FileReader import *
from pdb_parser import *
from pdb_writer import *
from single_gbsa_plotter import *

""" usage: FINAL_DECOMP_MMPBSA.dat your_GBSA_ligand.pdb your_GBSA_receptor.pdb"""


def main():
    file_reader = FileReader(sys.argv[3], sys.argv[2])
    decomp_reader(sys.argv[1], sys.argv[2], sys.argv[3], file_reader)
    lig_reader(sys.argv[2])
    rec_reader(sys.argv[3])
    lig_writer(sys.argv[2])
    rec_writer(sys.argv[3])
    plotter = Plotter(sys.argv[1], file_reader)
    plotter.plot()


if __name__ == '__main__':
    main()
