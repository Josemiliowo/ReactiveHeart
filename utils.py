import csv
import matplotlib.pyplot as plt
import pandas as pd

from biomarcador import Biomarcador

class Utils:
    @staticmethod
    def readCSVtoBiomarcador(filename):
        biomarcadores = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                nombre = row[0]
                enfermedades = row[1].split(".")  # Convert string to list
                valorES = float(row[2])
                valorEI = float(row[3])
                biomarcador = Biomarcador(nombre, enfermedades, [valorES, valorEI])
                biomarcadores.append(biomarcador)
        return biomarcadores

    @staticmethod
    def readCSVtoEstudio(filename):
        biomarcadoresEstudio = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                nombre = row[0]
                valor = row[1]
                pair = [nombre, valor]
                biomarcadoresEstudio.append(pair)
        return biomarcadoresEstudio

    @staticmethod
    def create_pie_chart(data):
        labels = data.keys()
        sizes = data.values()

        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

    @staticmethod
    def list_to_dict(list):
        list.insert(0, ["Biomarcadores", "Valores obtenidos"])
        dict_from_list = {item[0]: item[1] for item in list}
        return dict_from_list

    @staticmethod
    def csv_to_dataframe(filename):
        df = pd.read_csv(filename)
        return df

    @staticmethod
    def pair_exists(id, key):
        df = Utils.csv_to_dataframe('claves.csv')
        filtered_df = df[(df['ID'] == id) & (df['Key'] == key)]
        return not filtered_df.empty

    @staticmethod
    def get_paciente_and_path(id, key):
        df = Utils.csv_to_dataframe('claves.csv')
        filtered_df = df[(df['ID'] == id) & (df['Key'] == key)]

        if not filtered_df.empty:
            paciente = filtered_df['Paciente'].values[0]
            path = f'resultados{paciente}.csv'
            return paciente, path
        else:
            return None, None