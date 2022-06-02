from decomp_reader import *


def lig_writer(filename2):
    pdb_cont = open("plotted_gbsa.pdb", 'w')
    with open(filename2, "r") as template:
        for keys in lig_dec_residue.keys():
            for lines in template.readlines():
                if lines.split()[0] != 'ATOM':
                    continue
                if (str(lines.split()[3] + " " + str(lines[22:27].strip()))) in lig_dec_residue[keys]:
                    b_value = lig_dec_residue[keys][(lines.split()[3] + " " + str(lines[22:27].strip()))]
                    b_value = round(float(b_value), 2)
                    l_second_part = float(b_value)
                    pdb_cont.write(lines[0:62] + str(round(float(l_second_part), 2)) + f"      {keys}" '\n')

        pdb_cont.write(lines)
    pdb_cont.close()


def rec_writer(filename):
    pdb_cont = open("plotted_gbsa.pdb", 'a')
    with open(filename, "r") as template:
        for keys in recept_dec_residue.keys():
            for lines in template.readlines():
                if lines.split()[0] != 'ATOM':
                    continue
                elif (str(lines.split()[3] + " " + str(lines[22:27].strip()))) in recept_dec_residue[keys]:
                    b_value = recept_dec_residue[keys][(lines.split()[3] + " " + str(lines[22:27].strip()))]
                    b_value = round(float(b_value), 2)
                    l_second_part = float(b_value)
                    pdb_cont.write(lines[0:62] + str(round(float(l_second_part), 2)) + f"      {keys}" '\n')
        pdb_cont.write(lines)
    pdb_cont.close()
    print(recept_dec_residue)
