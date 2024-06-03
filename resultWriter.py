class ResultWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_to_json(self, freq, lambdas, rcs_values):
        with open(self.filename, 'w') as f:
            f.write("{\n")
            f.write("    \"freq\": [" + ', '.join(map(str, freq)) + '],\n')
            f.write("    \"lambda\": [" + ', '.join(map(str, lambdas)) + '],\n')
            f.write("    \"rcs\": [" + ', '.join(map(str, rcs_values)) + ']\n')
            f.write("}")