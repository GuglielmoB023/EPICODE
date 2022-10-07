import json
import statistics

def read_json(file_path):
    """
    Legge un file JSON e inserisce i dati in un dizionario
    :param file_path: file path of json
    :return: data read from file
    """
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

filename = '/Users/guglielmobenedetto/Documents/EPICODE/Settimana 2/Progetto/owid-covid-data.json'
dataset = read_json(filename)

""" STRUTTURA DEL DATASET
class 'dict'
dataset = { 'AFG' : {'continent': '...',
                     'location': '...',
                     'population': '...',
                     'data': [{'date': '...',
                               'total_case': '...',
                               ....,
                               },
                               {'date': '...',
                               'total_case': '...',
                               ....,
                               }]
                     },...
           { 'OWID_AFR' : {'...': '...',
                           '...': '...',
                           '...': '...',
                           '...': [{'...': '...',
                                    '...': '...',
                                    ....,
                                    },
                                    {'...': '...',
                                    '...': '...',
                                    ....,
                                    }]
                           },...                     
"""

#print(dataset)


def somma_paese(paese,parametro):
    """
    Creo una lista per poi sommare i dati di tutti i giorni registrati
    :param paese: paese su cui si vuole indagare
    :param parametro: variabile del paese su cui si vuole indagare
    :return: somma
    """
    list_p = []
    somma = 0
    for i in range(0, len(dataset[paese]['data'])):
        if (dataset[paese]['data'][i].get(parametro, None)) != None:
            list_p.append(dataset[paese]['data'][i].get(parametro))
    somma = somma + (dataset[paese]['data'][i].get(parametro))
    return somma


def media_paese(paese,parametro):
    """
    Creo una lista per calcolare la media dei dati di tutti i giorni registrati
    :param paese: paese su cui si vuole indagare
    :param parametro: variabile del paese su cui si vuole indagare
    :return: media
    """
    list_p = []
    for i in range(0, len(dataset[paese]['data'])):
        if (dataset[paese]['data'][i].get(parametro, None)) != None:
            list_p.append(dataset[paese]['data'][i].get(parametro))
    media = statistics.mean(list_p)
    return media


def deviazione_paese(paese,parametro):
    """
    Creo una lista per poi calcolare la deviazione standard dei dati di tutti i giorni registrati
    :param paese: paese su cui si vuole indagare
    :param parametro: variabile del paese su cui si vuole indagare
    :return: deviazione standard
    """
    list_p = []
    for i in range(0, len(dataset[paese]['data'])):
        if (dataset[paese]['data'][i].get(parametro, None)) != None:
            list_p.append(dataset[paese]['data'][i].get(parametro))
    deviazione = statistics.stdev(list_p)
    return deviazione


paese = 'FRA'
parametro = 'new_cases_per_million'
media_p1 = media_paese(paese,parametro)
somma_p1 = somma_paese(paese,parametro)
dev_p1 = deviazione_paese(paese,parametro)
print('La somma dei', parametro, 'in', paese, 'è:', int(somma_p1))
print('La media dei', parametro, 'in', paese, 'è:', int(media_p1))
print('La deviazione standard dei', parametro, 'in', paese, 'è:', round(dev_p1,2))

paese = 'ITA'
parametro = 'new_cases_per_million'
media_p2 = media_paese(paese,parametro)
somma_p2 = somma_paese(paese,parametro)
dev_p2 = deviazione_paese(paese,parametro)
print('La somma dei', parametro, 'in', paese, 'è:', int((somma_p2)))
print('La media dei', parametro, 'in', paese, 'è:', int((media_p2)))
print('La deviazione standard dei', parametro, 'in', paese, 'è:', round(dev_p2,2))


def somma_continente(continente,parametro):
    """
    Creo una lista per poi sommare i dati di tutti i giorni registrati
    :param continente: continente su cui si vuole indagare
    :param parametro: variabile del continente su cui si vuole indagare
    :return: somma
    """
    list_c = []
    somma = 0
    for i in dataset:
        if dataset[i].get('continent', 'errore') == continente:
            for g in range(0, len(dataset[i]['data'])):
                if (dataset[i]['data'][g].get(parametro, None)) != None:
                    list_c.append(dataset[i]['data'][g].get(parametro))
    somma = somma + (dataset[i]['data'][g].get(parametro))
    return somma


def media_continente(continente,parametro):
    """
    Creo una lista per calcolare la media dei dati di tutti i giorni registrati
    :param continente: continente su cui si vuole indagare
    :param parametro: variabile del continente su cui si vuole indagare
    :return: media
    """
    list_c = []
    for i in dataset:
        if dataset[i].get('continent', 'errore') == continente:
            for g in range(0, len(dataset[i]['data'])):
                if (dataset[i]['data'][g].get(parametro, None)) != None:
                    list_c.append(dataset[i]['data'][g].get(parametro))
    media = statistics.mean(list_c)
    return media


def deviazione_continente(continente,parametro):
    """
    Creo una lista per poi calcolare la deviazione standard dei dati di tutti i giorni registrati
    :param continente: continente su cui si vuole indagare
    :param parametro: variabile del continente su cui si vuole indagare
    :return: deviazione standard
    """
    list_c = []
    for i in dataset:
        if dataset[i].get('continent', 'errore') == continente:
            for g in range(0, len(dataset[i]['data'])):
                if (dataset[i]['data'][g].get(parametro, None)) != None:
                    list_c.append(dataset[i]['data'][g].get(parametro))
    deviazione = statistics.stdev(list_c)
    return deviazione


continente = 'North America'
parametro = 'total_cases_per_million'
somma_c1 = somma_continente(continente,parametro)
media_c1 = media_continente(continente,parametro)
dev_c1 = deviazione_continente(continente,parametro)
print('La somma dei', parametro, 'in', continente, 'è:', int(somma_c1))
print('La media dei', parametro, 'in', continente, 'è:', int(media_c1))
print('La deviazione standard dei', parametro, 'in', continente, 'è:', round(dev_c1,2))

continente = 'Asia'
parametro = 'total_cases_per_million'
somma_c2 = somma_continente(continente,parametro)
media_c2 = media_continente(continente,parametro)
dev_c2 = deviazione_continente(continente,parametro)
print('La somma dei', parametro, 'in', continente, 'è:', int(somma_c2))
print('La media dei', parametro, 'in', continente, 'è:', int(media_c2))
print('La deviazione standard dei', parametro, 'in', continente, 'è:', round(dev_c2,2))