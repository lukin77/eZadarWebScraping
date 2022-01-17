import pandas as pd
from collections import Counter

covid_news_indexes = []
vaccine_news_indexes = []
antimasker_news_indexes = []
antivakser_news_indexes = []
stopWords = []


def dataTransformation():
    # Remove ID column
    del data['ID']
    # Convert column's data to lower case
    data['TAG'] = data['TAG'].str.lower()
    data['POTPUNI TEKST'] = data['POTPUNI TEKST'].str.lower()
    data['NASLOV'] = data['NASLOV'].str.lower()
    # Remove time from date
    data['DATUM OBJAVLJIVANJA'] = data['DATUM OBJAVLJIVANJA'].str.split(' ')
    data['DATUM OBJAVLJIVANJA'] = data['DATUM OBJAVLJIVANJA'].str[0]
    # Split publish date into 3 columns
    data[['DAN', 'MJESEC', 'GODINA']
         ] = data['DATUM OBJAVLJIVANJA'].str.split('.', expand=True)


def covidNews():
    # TO DO: - add more key words
    covid_key_words = ['sars-cov-2', 'covid-19', 'corona', 'korona', 'koronavirus', 'korona-virus', 'epidemija', 'pandemija', 'samoizolacija', 'novozaražen', 'koronakriza',
                       'propusnica', 'e-propusnica', 'cjepivo', 'cijepljenje', 'lockdown', 'who', 'stožer civilne zaštite', 'vijesti iz stožera', 'omikron', 'delta soj', 'flurona', 'covid potvrda', 'novih slučajeva']

    for key_word in covid_key_words:
        # Search for key word
        naslovi = data[data['NASLOV'].str.contains(key_word)]
        potpuni_tekst = data[data['POTPUNI TEKST'].str.contains(
            key_word, na=False)]
        tag = data[data['TAG'].str.contains(key_word)]
        # Add indexes to variables
        index_naslov = naslovi.index
        index_potpuni_tekst = potpuni_tekst.index
        index_tag = tag.index

        # Add index to list (without duplicates) for selected columns
        for index in index_naslov:
            if index not in covid_news_indexes:
                covid_news_indexes.append(index)
        for index in index_potpuni_tekst:
            if index not in covid_news_indexes:
                covid_news_indexes.append(index)
        for index in index_tag:
            if index not in covid_news_indexes:
                covid_news_indexes.append(index)

    print('Broj vijesti vezanih za korona tematiku:', len(covid_news_indexes))


def vaccineNews():
    # TO DO: - add more key words
    vaccine_key_words = ['cijepljenje', 'procijepljenost', 'bionTech', 'pfizer', 'sputnik v', 'astrazeneca', 'moderna', 'spikevax',
                         'comirnaty', 'vaxzevria', 'johnson&johnson', 'janssen', 'cjepivo', 'javno-cijepljenje', 'docjepljivanje', 'doza cjepiva']

    for key_word in vaccine_key_words:
        # Search for key word
        naslovi = data[data['NASLOV'].str.contains(key_word)]
        potpuni_tekst = data[data['POTPUNI TEKST'].str.contains(
            key_word, na=False)]
        tag = data[data['TAG'].str.contains(key_word)]
        # Add indexes to variables
        index_naslov = naslovi.index
        index_potpuni_tekst = potpuni_tekst.index
        index_tag = tag.index

        # Add index to list (without duplicates)
        for index in index_naslov:
            if index not in vaccine_news_indexes:
                vaccine_news_indexes.append(index)

        for index in index_potpuni_tekst:
            if index not in vaccine_news_indexes:
                vaccine_news_indexes.append(index)

        for index in index_tag:
            if index not in vaccine_news_indexes:
                vaccine_news_indexes.append(index)

    print('Broj vijesti vezanih za cijepljenje:', len(vaccine_news_indexes))


def antimaskerNews():
    # TO DO: - add more key words
    antimasker_key_words = ['antimasker',
                            'protiv maski', 'protiv nošenja maske']

    for key_word in antimasker_key_words:
        # Search for key word

        naslovi = data[data['NASLOV'].str.contains(key_word)]
        potpuni_tekst = data[data['POTPUNI TEKST'].str.contains(
            key_word, na=False)]
        tag = data[data['TAG'].str.contains(key_word)]
        # Add indexes to variables
        index_naslov = naslovi.index
        index_potpuni_tekst = potpuni_tekst.index
        index_tag = tag.index

        # Add index to list (without duplicates)
        for index in index_naslov:
            if index not in antimasker_key_words:
                antimasker_news_indexes.append(index)

        for index in index_potpuni_tekst:
            if index not in antimasker_key_words:
                antimasker_news_indexes.append(index)

        for index in index_tag:
            if index not in antimasker_key_words:
                antimasker_news_indexes.append(index)

    print('Broj vijesti vezanih za antimaskere:', len(antimasker_news_indexes))


def antivakserNews():
    # TO DO: - add more key words
    antivakser_key_words = ['antivakser', 'protiv cijepiva',
                            'protiv cijepljenja', 'odbijanje cijepljenja', 'odbija se cijepiti']

    for key_word in antivakser_key_words:
        # Search for key word
        naslovi = data[data['NASLOV'].str.contains(key_word)]
        potpuni_tekst = data[data['POTPUNI TEKST'].str.contains(
            key_word, na=False)]
        tag = data[data['TAG'].str.contains(key_word)]
        # Add indexes to variables
        index_naslov = naslovi.index
        index_potpuni_tekst = potpuni_tekst.index
        index_tag = tag.index

        # Add index to list (without duplicates)
        for index in index_naslov:
            if index not in antivakser_key_words:
                antivakser_news_indexes.append(index)

        for index in index_potpuni_tekst:
            if index not in antivakser_key_words:
                antivakser_news_indexes.append(index)

        for index in index_tag:
            if index not in antivakser_key_words:
                antivakser_news_indexes.append(index)

    print('Broj vijesti vezanih za antivaksere:', len(antivakser_news_indexes))


def newsDaily():
    # Create dataframe with dates
    date_df = pd.DataFrame(pd.date_range(
        start='01.01.2021', periods=365).strftime('%d.%m.%Y'), columns=['Datum'])
    brojObjavaNaDan = []
    brojCovidObjavaNaDan = []

    # Find number of news for each date
    for datum in date_df['Datum']:
        brojObjavaNaDan.append(
            data['DATUM OBJAVLJIVANJA'].isin([datum]).sum(axis=0))
        count = 0
        # Find number of covid news
        for index in covid_news_indexes:
            if(data.iloc[index]['DATUM OBJAVLJIVANJA'] == datum):
                count += 1
        brojCovidObjavaNaDan.append(count)

    # Add new columns to dataframe
    date_df['Broj svih objava na portalu'] = brojObjavaNaDan
    date_df['Broj objava vezanih za koronu'] = brojCovidObjavaNaDan
    # print(date_frame)
    # Export dataframe to Excel
    date_df.to_excel("./rezultati/Objave_po_danima.xlsx")


def newMonthly():
    # Create dataframe with months
    month_df = pd.DataFrame(pd.date_range(
        start='01.01.2021', end='31.12.2021', freq='M').strftime('%m'), columns=['MJESEC'])

    brojObjavaPoMjesecu = []
    brojCovidObjavaPoMjesecu = []
    # Find number of news for each month
    for misec in month_df['MJESEC']:
        brojObjavaPoMjesecu.append(data['MJESEC'].isin([misec]).sum(axis=0))
        count = 0
        # Find number of covid news
        for index in covid_news_indexes:
            if(data.iloc[index]['MJESEC'] == misec):
                count += 1
        brojCovidObjavaPoMjesecu.append(count)

    month_df['Ukupan broj objava'] = brojObjavaPoMjesecu
    month_df['Broj objava vezanih za koronu'] = brojCovidObjavaPoMjesecu
    month_df.to_excel("./rezultati/Objave_po_mjesecima.xlsx")


def newsCategory():
    category_df = pd.DataFrame(
        data['KATEGORIJA'].unique(), columns=['KATEGORIJA'])
    brojObjavaPoKategoriji = []
    brojCovidObjavaPoKategoriji = []
    # Find number of news for each category
    for kategorija in category_df['KATEGORIJA']:
        brojObjavaPoKategoriji.append(
            data['KATEGORIJA'].isin([kategorija]).sum(axis=0))
        count = 0
        # Find number of covid news
        for index in covid_news_indexes:
            if(data.iloc[index]['KATEGORIJA'] == kategorija):
                count += 1
        brojCovidObjavaPoKategoriji.append(count)

    category_df['Broj objava'] = brojObjavaPoKategoriji
    category_df['Broj objava vezanih za koronu'] = brojCovidObjavaPoKategoriji

    category_df.to_excel("./rezultati/Objave_po_kategorijama.xlsx")


def readStopWords():
    with open('./podaci/stopWords.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            stopWords.append(line.strip('\n'))


def mostUsedWords():
    covidData = data.iloc[covid_news_indexes]
    specialCharacters = [',', '\.', '\#', '\(', '\)', '\/', '\*', '\$', '\&', '\;',
                         '\:', '\"', '\'', '“', '”', '‘', '’', '“', '„', '\!', '\?', '%', '-', '–']
    covidData = covidData.replace(specialCharacters, ' ', regex=True)

    # Create dataframe with months
    month_df = pd.DataFrame(pd.date_range(
        start='01.01.2021', end='31.12.2021', freq='M').strftime('%m'), columns=['MJESEC'])

    for misec in month_df['MJESEC']:
        temp_df = covidData[covidData['MJESEC'] == misec]
        join_df = temp_df["NASLOV"] + temp_df["POTPUNI TEKST"] + temp_df["TAG"]
        mostUsedWords = Counter(" ".join(join_df).split()).most_common(150)

        for toupleOfUsedWord in list(mostUsedWords):
            if(toupleOfUsedWord[0] in stopWords):
                mostUsedWords.remove(toupleOfUsedWord)

        word_df = pd.DataFrame(mostUsedWords[:25], columns=[
                               'RIJEČ', 'BROJ POJAVLJIVANJA'])
        word_df.to_excel('./rezultati/top_rijeci/Top_rijeci_'+misec+'.xlsx')


def jaccardIndex(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(set(list1)) + len(set(list2))) - intersection
    return float(intersection) / union


def jaccardIndexCalculate():
    import os
    entries = os.listdir('./rezultati/top_rijeci/')

    words_list = []
    jaccard_list = []
    for entry in entries:
        df = pd.read_excel('./rezultati/top_rijeci/' + entry)
        words_list.append(list(df['RIJEČ']))

    for i in range(len(words_list)):
        if (i < 10):
            jaccard_list.append(round(jaccardIndex(words_list[i], words_list[i+1]), 4))

    # Create dataframe with months
    months_df = pd.DataFrame(pd.date_range(start='01.02.2021', periods=10), columns=['MJESEC'])
    months_df['MJESEC'] = months_df['MJESEC'].apply(str)
    months_df['MJESEC'] = months_df['MJESEC'].str.split(' ')
    months_df['MJESEC'] = months_df['MJESEC'].str[0]
    months_df['MJESEC'] = months_df['MJESEC'].str.split('-')
    months_df['MJESEC'] = months_df['MJESEC'].str[2]
    months_df['JACCARD INDEX'] = jaccard_list
    months_df.to_excel('./rezultati/jaccard_index.xlsx')


if __name__ == '__main__':
    # Read csv
    data = pd.read_csv("./podaci/eZadarPodaci.csv")
    print('Ukupan broj objava na portalu eZadar u 2021. godini:',
          data['ID'].count())

    dataTransformation()
    covidNews()
    vaccineNews()
    antimaskerNews()
    antivakserNews()
    newsDaily()
    newMonthly()
    newsCategory()
    readStopWords()
    mostUsedWords()
    jaccardIndexCalculate()
