class FileReader:
    rec_num = [None]
    lig_num = [None]

    def __init__(self, receptor=None, ligand=None):
        self.rec_file = open(receptor, 'r')
        self.lig_file = open(ligand, 'r')
        self.fetch_nums(self.rec_file, self.rec_num)
        self.fetch_nums(self.lig_file, self.lig_num)

    def fetch_nums(self, file, num):
        for lines in file.readlines():
            if 'ATOM' not in lines:
                continue
            if 'ATOM' in lines:
                num[0] = lines[22:27].strip()
            break