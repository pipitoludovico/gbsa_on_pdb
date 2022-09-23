from FileReader import *
import matplotlib.pyplot as plt
import pandas as pd


class Plotter:

    def __init__(self, filename, file_reader):
        self.filename = filename
        self.file_reader = file_reader

    def plot(self):

        decomp_purged = open("total_purged.csv", 'w')
        with open(self.filename, 'r') as f:
            for l in f.readlines():
                decomp_purged.writelines(l)
                if l == "\n" or l == " ":
                    break
            decomp_purged.close()

        with open("total_purged.csv", 'rU') as purged:
            for lines in purged.readlines():
                try:
                    header = 6
                    if lines == " " or lines == "" or lines == "\n":
                        break
                    if lines[8:9] == "L":
                        df = pd.read_csv('total_purged.csv', sep=',', header=header, usecols=['Location', 'TOTAL'])
                        df = df.loc[(df['TOTAL'] <= -0.25) & df['Location'].str.startswith("L")]
                        df.dropna(how='all', inplace=True)
                        df.set_index('Location', inplace=True)
                        df.index = df.index.str.split()
                        df.index = df.index.str[1] + ' ' + ((df.index.str[2].astype(int)) + (
                                int(str(FileReader.starting_lig[0]).split()[1]) - 1)).astype(str)

                    if lines[8:9] == "R":
                        dfr = pd.read_csv('total_purged.csv', sep=',', header=header, usecols=['Location', 'TOTAL'])
                        dfr = dfr.loc[(dfr['TOTAL'] <= -0.25) & dfr['Location'].str.startswith("R")]
                        dfr.dropna(how='all', inplace=True)
                        dfr.set_index('Location', inplace=True)
                        dfr.index = dfr.index.str.split()
                        dfr.index = dfr.index.str[1] + ' ' + ((dfr.index.str[2].astype(int)) + (
                                int(str(FileReader.starting_rec[0]).split()[1]) - 1)).astype(str)
                except:
                    header = 5
                    if lines == " " or lines == "" or lines == "\n":
                        break
                    if lines[8:9] == "L":
                        df = pd.read_csv('total_purged.csv', sep=',', header=header, usecols=['Location', 'TOTAL'])
                        df = df.loc[(df['TOTAL'] <= -0.25) & df['Location'].str.startswith("L")]
                        df.dropna(how='all', inplace=True)
                        df.set_index('Location', inplace=True)
                        df.index = df.index.str.split()
                        df.index = df.index.str[1] + ' ' + ((df.index.str[2].astype(int)) + (
                                int(str(FileReader.starting_lig[0]).split()[1]) - 1)).astype(str)

                    if lines[8:9] == "R":
                        dfr = pd.read_csv('total_purged.csv', sep=',', header=header, usecols=['Location', 'TOTAL'])
                        dfr = dfr.loc[(dfr['TOTAL'] <= -0.25) & dfr['Location'].str.startswith("R")]
                        dfr.dropna(how='all', inplace=True)
                        dfr.set_index('Location', inplace=True)
                        dfr.index = dfr.index.str.split()
                        dfr.index = dfr.index.str[1] + ' ' + ((dfr.index.str[2].astype(int)) + (
                                int(str(FileReader.starting_rec[0]).split()[1]) - 1)).astype(str)

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
                print(
                    "receptor dataframe empty: check the total_purged.csv or check if the file has been read till the end")
