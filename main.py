import sys

from FileReader import *
from pdb_parser import *
from pdb_writer import *
from single_gbsa_plotter import *

""" usage: FINAL_DECOMP_MMPBSA.dat your_GBSA_ligand.pdb your_GBSA_receptor.pdb"""

cwd = os.getcwd()
script_dir = os.path.dirname(__file__)

data = "FINAL_DECOMP_MMPBSA.dat"

if len(sys.argv) > 1:
    if sys.argv[1] == 'unify':
        os.system('pdb_seg -L ligand.pdb > ligandL.pdb')
        os.system('pdb_seg -R receptor.pdb > receptorR.pdb')

        ligand = "ligandL.pdb"
        receptor = "receptorR.pdb"
    else:
        print('add "unify" to set a single segid for the ligand and a single segid for the receptor')
else:
    ligand = "ligand.pdb"
    receptor = "receptor.pdb"

ligand_abs_file_path = os.path.join(script_dir, ligand)
receptor_abs_file_path = os.path.join(script_dir, receptor)
data_abs_file_path = os.path.join(script_dir, data)


def main():
    file_reader = FileReader(receptor_abs_file_path, ligand_abs_file_path)
    decomp_reader(data_abs_file_path, ligand_abs_file_path, receptor_abs_file_path, file_reader)
    lig_reader(ligand_abs_file_path)
    rec_reader(receptor_abs_file_path)
    lig_writer(ligand_abs_file_path)
    rec_writer(receptor_abs_file_path)
    plotter = Plotter(data_abs_file_path, file_reader)
    plotter.plot()


if __name__ == '__main__':
    main()
