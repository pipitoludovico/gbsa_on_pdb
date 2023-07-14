class DataWriter:
    def __init__(self, ligandList, receptorList, ligandDecompResults, recDecompResults):
        self.ligandList = ligandList
        self.receptorList = receptorList
        self.ligandDecompResults = ligandDecompResults
        self.recDecompResults = recDecompResults
        self.files = ['ligand.dat', 'receptor.dat']
        self.results = [ligandDecompResults, recDecompResults]
        self.WriteDat()
        self.WriteGBSAonPDB()

    def WriteDat(self):

        for file_name, decomp_results in zip(self.files, self.results):
            i = 0
            with open(file_name, 'w') as file:
                file.write('Residue\tGBSA\n')
                if file_name == 'ligand.dat':
                    data_dict = self.ligandList
                elif file_name == 'receptor.dat':
                    data_dict = self.receptorList

                for segid, res_list in data_dict.items():
                    for res in res_list:
                        file.write(res + "\t" + str(decomp_results[i]) + '\n')
                        i += 1

    def WriteGBSAonPDB(self):
        with open('ligand.pdb', 'r') as input_file, open('GBSA_on_PDB.pdb', 'w') as output_file:
            residuo_corrente = None
            indice_valore = 0

            for line in input_file:
                if line.startswith('ATOM') or line.startswith('HETATM'):
                    residuo = line[17:26].strip()

                    if residuo != residuo_corrente:
                        occupancy_value = self.ligandDecompResults[indice_valore]
                        indice_valore += 1
                        residuo_corrente = residuo

                    line = line[:60] + " " + str(round(occupancy_value, 2)) + line[66:]
                output_file.write(line)

        with open('receptor.pdb', 'r') as input_file, open('GBSA_on_PDB.pdb', 'a') as output_file:
            residuo_corrente = None
            indice_valore = 0

            for line in input_file:
                if line.startswith('ATOM') or line.startswith('HETATM'):
                    residuo = line[17:26].strip()

                    if residuo != residuo_corrente:
                        occupancy_value = self.recDecompResults[indice_valore]
                        indice_valore += 1
                        residuo_corrente = residuo

                    line = line[:60] + " " + str(round(occupancy_value, 2)) + line[66:]
                output_file.write(line)
