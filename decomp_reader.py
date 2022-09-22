import os

lig_dec_residue = {}
recept_dec_residue = {}
lig_num = []
rec_num = []


def decomp_reader(datfile, ligand, receptor, file_reader):
    # os.system(f"cp {datfile}"  " FINAL_MMPBSA_bk.dat")
    os.system(f"sed -i 's/HSP/HIS/g' {datfile}")
    os.system(f"sed -i 's/HSE/HIS/g' {datfile}")
    os.system(f"sed -i 's/HSD/HIS/g' {datfile}")

    with open(ligand, 'r') as l:
        header_l = l.readlines()[1:]
        for line_lig in header_l:
            if line_lig.split()[0] == "ATOM":
                if line_lig[22:27].strip() not in lig_num:
                    lig_num.append(line_lig[22:27].strip())
                if line_lig[72:75].strip() not in lig_dec_residue:
                    lig_dec_residue[str(line_lig[72:75].strip())] = {}
                if (line_lig.split()[3] + " " + line_lig[22:27].strip()) not in lig_dec_residue[
                    str(line_lig[72:75].strip())]:
                    lig_dec_residue[str(line_lig[72:75].strip())][
                        line_lig.split()[3] + " " + line_lig[22:27].strip()] = 0

    with open(receptor, 'r') as r:
        header_r = r.readlines()[1:]
        for line_r in header_r:
            if line_r.split()[0] == "ATOM":
                if line_r[22:27].strip() not in rec_num:
                    rec_num.append(line_r[22:27].strip())
                if line_r[72:75].strip() not in recept_dec_residue:
                    recept_dec_residue[str(line_r[72:75].strip())] = {}
                if (line_r.split()[3] + " " + line_r[22:27].strip()) not in recept_dec_residue[
                    str(line_r[72:75].strip())]:
                    recept_dec_residue[str(line_r[72:75].strip())][line_r.split()[3] + " " + line_r[22:27].strip()] = 0

    with open(datfile, 'r') as f:
        noheader = f.readlines()[8:]

        for lines in noheader:
            if lines == "" or lines == " " or lines == "\n":
                break
            elif lines.split(",")[1][0] == "L":
                x = 0
                for key in lig_dec_residue.keys():
                    if (lines.split()[0]) + " " + lig_num[x] in lig_dec_residue[key]:
                        lig_dec_residue[key][(lines.split()[0]) + " " + lig_num[x]] = (lines.split(",")[17])
                    x += 1

        for lines in noheader:
            if lines == "" or lines == " " or lines == "\n":
                break
            elif lines.split(",")[1][0] == "R":
                y = 0
                for key in recept_dec_residue.keys():
                    if (lines.split()[0]) + " " + rec_num[y] in recept_dec_residue[key]:
                        recept_dec_residue[key][(lines.split()[0]) + " " + rec_num[y]] = (lines.split(",")[17])
                    y += 1

    return recept_dec_residue, lig_dec_residue
