import requests

class DataLoader:
    def __init__(self, url):
        self.url = url

    def parse_txt(self, variant_number):
        response = requests.get(self.url)
        lines = response.text.split('\n')
        variant_data = lines[variant_number - 1].split('; ')
        D = float(variant_data[0].split('=')[1])
        fmin = float(variant_data[1].split('=')[1].replace('e9', '')) * 1e9
        fmax = float(variant_data[2].split('=')[1].replace('e9', '')) * 1e9
        return D, fmin, fmax