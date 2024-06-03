from dataLoader import DataLoader
from RCS import RCS
from resultWriter import ResultWriter
from plotter import Plotter
import numpy as np

def main():
    url = "https://jenyay.net/uploads/Student/Modelling/task_rcs_01.txt"
    variant_number = 12
    
    loader = DataLoader(url)
    D, fmin, fmax = loader.parse_txt(variant_number)

    frequencies = np.linspace(fmin, fmax, num=500)
    rcs_calculator = RCS(D / 2)
    freq_list, lambda_list, rcs_list = [], [], []

    for freq in frequencies:
        rcs = rcs_calculator.calculate_rcs(freq)
        freq_list.append(freq)
        lambda_list.append(3e8 / freq)
        rcs_list.append(rcs)

    writer = ResultWriter("rcs_results.json")
    writer.write_to_json(freq_list, lambda_list, rcs_list)

    plotter = Plotter()
    plotter.plot_rcs_vs_frequency(freq_list, rcs_list)

if __name__ == "__main__":
    main()