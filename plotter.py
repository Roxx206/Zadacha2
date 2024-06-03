import matplotlib.pyplot as plt

class Plotter:
    def plot_rcs_vs_frequency(self, freq, rcs_values):
        plt.figure(figsize=(10, 6))
        plt.plot(freq, rcs_values, color='b', linestyle='-')
        plt.xlabel('Частота (Гц)')
        plt.ylabel('ЭПР (м^2)')
        plt.title('ЭПР vs. Частота')
        #plt.xscale('log')
        plt.grid(True)
        plt.show()