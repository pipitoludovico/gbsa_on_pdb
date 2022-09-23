from FileReader import *
import matplotlib.pyplot as plt
import pandas as pd


class Plotter:

    def __init__(self, filename, file_reader):
        self.filename = filename
        self.file_reader = file_reader

    def plot(self):

        decomp_purged = open("total_purged.csv", 'w')
        with open(self.filename) as file:
            text = "".join(file.read().upper().split('TOTAL ENERGY DECOMPOSITION')[1:]).strip().split("SIDECHAIN")[0]
            decomp_purged.writelines(text)


        with open("total_purged.csv", 'r') as purged:
            noheader = purged.readlines()
            header = 1
            for lines in noheader:
                if lines == ":\n":
                    continue
                if lines == " ":
                    break
                if lines.split(",")[1].split(" ")[0] == "L":
                    df = pd.read_csv('total_purged.csv', sep=',', header=header, usecols=['LOCATION', 'TOTAL'])
                    df = df.loc[(df['TOTAL'] <= -0.25) & df['LOCATION'].str.startswith("L")]
                    df.dropna(how='all', inplace=True)
                    df.set_index('LOCATION', inplace=True)
                    df.index = df.index.str.split()
                    df.index = df.index.str[1] + ' ' + ((df.index.str[2].astype(int)) + (int(str(FileReader.starting_lig[0]).split()[1]) - 1)).astype(str)

                if lines.split(",")[1].split(" ")[0] == "R":
                    dfr = pd.read_csv('total_purged.csv', sep=',', header=header, usecols=['LOCATION', 'TOTAL'])
                    dfr = dfr.loc[(dfr['TOTAL'] <= -0.25) & dfr['LOCATION'].str.startswith("R")]
                    dfr.dropna(how='all', inplace=True)
                    dfr.set_index('LOCATION', inplace=True)
                    dfr.index = dfr.index.str.split()
                    dfr.index = dfr.index.str[1] + ' ' + ((dfr.index.str[2].astype(int)) + (int(str(FileReader.starting_rec[0]).split()[1]) - 1)).astype(str)
        try:
            plt.style.use('ggplot')  # uses gnuplot style
            df.plot(y='TOTAL', kind='bar', legend=False)
            plt.xlabel('Residues', labelpad=30)
            plt.ylabel('Kcal/mol', labelpad=15)
            plt.tight_layout()
            plt.savefig('ligand_gbsa.jpg', dpi=300)
            plt.show()
            plt.close()
        except:
            print("ligand dataframe empty: check the total_purged.csv or check if the file has been read till the end")

        try:
            dfr.plot(y='TOTAL', kind='bar', legend=False)
            plt.xlabel('Residues', labelpad=30)
            plt.ylabel('Kcal/mol', labelpad=15)
            plt.tight_layout()
            plt.savefig('receptor_gbsa.jpg', dpi=300)
            plt.show()
            plt.close()
        except:
            print("receptor dataframe empty: check the total_purged.csv or check if the file has been read till the end")


