import re


def join_jsons(json_f_1, json_f_2):
    """Opens files, reads, removes, them and
    combines it all in one line, and then write
    to a new full json file

    :param file1: 'winedata_1.json'
    :param file2: 'winedata_2.json'
    :return: None
    """
    with open(json_f_1, 'r', encoding='utf-8') as f1, \
            open(json_f_2, 'r', encoding='utf-8') as f2:
        t1, t2 = f1.read().replace("]", ""), f2.read().replace("[", "")
        concat_text = t1 + "," + t2

    with open('winedata_full.json', 'w', encoding='utf-8') as full_json_file_wr:
        full_json_file_wr.write(concat_text)

    return concat_text


def extraction_data_between_braces(concat_json_file):
    """The regex pattern allows us to get a list
    of elements that are between brackets

    :param concat_json_file:
    :return: keys, by_elems
    """
    json = concat_json_file.replace("null", '"0"')
    print(json[:1000], end="\n")
    pattern1 = r"\{(.*?)\}"
    rows_between_braces = re.findall(pattern1, json)
    for i, e in enumerate(rows_between_braces):
        print(e)
        if i == 0:
            break

    keys = [
        'points',
        'title',
        'description',
        'taster_name',
        'taster_twitter_handle',
        'price',
        'designation',
        'variety',
        'region_1',
        'region_2',
        'province',
        'country',
        'winery',
         ]
    return keys, rows_between_braces


def get_wine_data(keys, datas_btw_braces):
    """

    :param keys: different keys in each row
    :param datas_btw_braces: {data1}, {bata2}... list without {}
    :return:
    """
    wine_data = []
    for row in datas_btw_braces:

        pattern2 = r'\: \"(.*?)\"'
        values = re.findall(pattern2, row)
        values[0] = int(values[0])

        if '"price": "0"' not in row:
            pattern3 = r'\"price\"\: (.*?)\,'
            price = list(map(int, re.findall(pattern3, row)))
            if price[0] > 0:
                values.insert(5, price[0])
        temp_dict = dict(zip(keys, values))
        wine_data.append(temp_dict)

    print(1)
    for i in wine_data[:10]:
        print(i)

    wine_data = sorted(wine_data, key=lambda x: int(x['price']), reverse=True)

    print(2)
    for i in wine_data[:10]:
        print(i)

    with open('winedata_full.json', 'w', encoding='utf-8') as out:
        json = f'{wine_data}'
        out.write(json)

    # return wine_data

if __name__ == '__main__':

    json_file_1 = 'winedata_1.json'
    json_file_2 = 'winedata_2.json'
    full_json = 'winedata_full.json'

    varietys = ['Gew\\u00fcrztraminer',
                'Riesling',
                'Merlot',
                'Tempranillo',
                'Red Blend',
                'Madera']

    concat_text = join_jsons(json_file_1, json_file_2)
    keys, datas_betw_braces = extraction_data_between_braces(concat_text)
    wine_data = get_wine_data(keys, datas_betw_braces)
