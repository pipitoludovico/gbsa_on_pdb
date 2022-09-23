class FileReader:
    receptor_id = {}
    ligand_id = {}
    starting_rec = []
    starting_lig = []

    def __init__(self, receptor=None, ligand=None):
        self.rec_file = open(receptor, 'r')
        self.lig_file = open(ligand, 'r')

        for line in self.rec_file:
            if line.split()[0] == "" or line.split()[0] == "\n":
                continue
            if line.split()[0].startswith("ATOM"):
                if line.split()[3] + " " + line[22:27].strip() not in self.starting_rec:
                    self.starting_rec.append(line.split()[3] + " " + line[22:27].strip())
                else:
                    continue
                if line[72:75].strip() not in self.receptor_id:
                    self.receptor_id[str(line[72:75].strip())] = {}

        for line in self.lig_file:
            if line.split()[0] == "" or line.split()[0] == "\n":
                continue
            if line.split()[0].startswith("ATOM"):
                if line.split()[3] + " " + line[22:27].strip() not in self.starting_lig:
                    self.starting_lig.append(line.split()[3] + " " + line[22:27].strip())
                else:
                    continue
                if line[72:75].strip() not in self.ligand_id:
                    self.ligand_id[str(line[72:75].strip())] = {}

        # print(self.starting_rec)
        # print(self.starting_lig)
