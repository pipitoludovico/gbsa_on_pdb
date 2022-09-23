from FileReader import *
import os


def decomp_reader(datfile):
    os.system(f"sed -i 's/HSP/HIS/g' {datfile}")
    os.system(f"sed -i 's/HSE/HIS/g' {datfile}")
    os.system(f"sed -i 's/HSD/HIS/g' {datfile}")

    with open(datfile, 'r') as f:
        noheader = f.readlines()[7:]

        for key in FileReader.receptor_id.keys():
            x = 0
            for lines in noheader:
                if lines == "" or lines == " " or lines == "\n":
                    break
                if lines.split()[1].split(',')[1] == "R":
                    FileReader.receptor_id[key][FileReader.starting_rec[x]] = (float(lines.split(",")[17]))
                    x += 1

        for key in FileReader.ligand_id.keys():
            y = 0
            for lines in noheader:
                if lines == "" or lines == " " or lines == "\n":
                    break
                if lines.split()[1].split(',')[1] == "L":
                    FileReader.ligand_id[key][FileReader.starting_lig[y]] = (float(lines.split(",")[17]))
                    y += 1

    return FileReader.receptor_id, FileReader.ligand_id
