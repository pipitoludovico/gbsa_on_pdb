import os


def lig_reader(filename2):
    os.system(f"cp {filename2}" f" {filename2}" "_bk")
    os.system(f"sed -i 's/HSP/HIS/g' {filename2}")
    os.system(f"sed -i 's/HSE/HIS/g' {filename2}")
    os.system(f"sed -i 's/HSD/HIS/g' {filename2}")


def rec_reader(filename):
    os.system(f"cp {filename}" f" {filename}" "_bk")
    os.system(f"sed -i 's/HSP/HIS/g' {filename}")
    os.system(f"sed -i 's/HSE/HIS/g' {filename}")
    os.system(f"sed -i 's/HSD/HIS/g' {filename}")
