from collections import Counter


class Estudio:
    def __init__(self, nombre, fecha, biomarcadores, db, comentario):
        self.nombre = nombre
        self.fecha = fecha
        self.biomarcadores = biomarcadores
        # [Nombre, value]
        self.db = db
        # [Biomarcador*]
        self.comentario = comentario


    def addBiomarcador(self, biomarcador):
        self.biomarcadores.append(biomarcador)

    def runStudyProp(self):
        results = []
        deviations = []
        for biomarcador in self.biomarcadores:
            for biomarcadorDB in self.db:
                if biomarcadorDB.getNombre() == biomarcador[0]:
                    if not float(biomarcadorDB.getValorEstable()[0]) <= float(biomarcador[1]) <= float(biomarcadorDB.getValorEstable()[1]):
                        #results.append(biomarcadorDB.getEnfermedades())
                        range_val = float(biomarcadorDB.getValorEstable()[1]) - float(
                            biomarcadorDB.getValorEstable()[0])
                        if float(biomarcador[1]) < float(biomarcadorDB.getValorEstable()[0]):
                            difference = float(biomarcadorDB.getValorEstable()[0]) - float(biomarcador[1])
                        else:
                            difference = float(biomarcador[1]) - float(biomarcadorDB.getValorEstable()[1])
                        deviation = (difference / range_val) * 100
                        deviations.append((biomarcadorDB.getEnfermedades(), round(deviation, 2)))

        for deviation in deviations:
            for disease in deviation[0]:
                results.append([disease, deviation[1]])

        resultList = {}
        for item in results:
            if item[0] in resultList:
                resultList[item[0]] += item[1]
            else:
                resultList[item[0]] = item[1]

        # flattened_results = [item for sublist in results for item in sublist]
        # directoryDiseases = dict(Counter(flattened_results))
        # for value in directoryDiseases:
        #     significance = directoryDiseases[value] / len(flattened_results) * 100
        #     directoryDiseases[value] = round(significance, 2)
        # print(flattened_results)

        total = sum(resultList.values())
        for key in resultList:
            resultList[key] = (resultList[key] / total) * 100

        return resultList


    def runStudyNonProp(self):
        results = []
        deviations = []
        for biomarcador in self.biomarcadores:
            for biomarcadorDB in self.db:
                if biomarcadorDB.getNombre() == biomarcador[0]:
                    if not float(biomarcadorDB.getValorEstable()[0]) <= float(biomarcador[1]) <= float(biomarcadorDB.getValorEstable()[1]):
                        results.append(biomarcadorDB.getEnfermedades())


        flattened_results = [item for sublist in results for item in sublist]
        directoryDiseases = dict(Counter(flattened_results))
        for value in directoryDiseases:
            significance = directoryDiseases[value] / len(flattened_results) * 100
            directoryDiseases[value] = round(significance, 2)
        print(flattened_results)

        return directoryDiseases

    def setComment(self, comment):
        self.comentario = comment

    def getComment(self):
        return self.comentario
