from decomp_reader import *


def lig_writer(filename2):
    pdb_cont = open("plotted_gbsa.pdb", 'w')
    with open(filename2, "r") as template:
        for keys, values in FileReader.ligand_id.items():
            for lines in template.readlines():
                if lines.split()[0] != 'ATOM':
                    continue
                if (str(lines.split()[3] + " " + str(lines[22:27].strip()))) in FileReader.ligand_id[keys]:
                    b_value = FileReader.ligand_id[keys][(lines.split()[3] + " " + str(lines[22:27].strip()))]
                    b_value = round(float(b_value), 1)
                    l_second_part = float(b_value)
                if str(l_second_part).startswith("-"):
                    pdb_cont.write(lines[0:62] + str(round(float(l_second_part), 2)) + f"     {keys}" '\n')
                else:
                    pdb_cont.write(lines[0:62] + str(round(float(l_second_part), 2)) + f"      {keys}" '\n')
        pdb_cont.close()


def rec_writer(filename):
    pdb_cont = open("plotted_gbsa.pdb", 'a')
    with open(filename, "r") as template:
        for keys, values in FileReader.receptor_id.items():
            for lines in template.readlines():
                if lines.split()[0] != 'ATOM':
                    continue
                if (str(lines.split()[3] + " " + str(lines[22:27].strip()))) in FileReader.receptor_id[keys]:
                    b_value = FileReader.receptor_id[keys][(lines.split()[3] + " " + str(lines[22:27].strip()))]
                    b_value = round(float(b_value), 1)
                    l_second_part = float(b_value)
                if str(l_second_part).startswith("-"):
                    pdb_cont.write(lines[0:62] + str(round(float(l_second_part), 2)) + f"     {keys}" '\n')
                else:
                    pdb_cont.write(lines[0:62] + str(round(float(l_second_part), 2)) + f"      {keys}" '\n')
        pdb_cont.close()
