import collections
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
    pattern_1 = r"\{(.*?)\}"
    rows_between_braces = re.findall(pattern_1, json)

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


def get_wine_data(list_keys, datas_btw_braces):
    """return a list of dicts data framed by braces

    :param keys: different keys in each row
    :param datas_btw_braces: {data1}, {bata2}... list without {}
    :return: datas for each wine
    """
    list_wine_data = []
    for row in datas_btw_braces:
        pattern_2 = r'\: \"(.*?)\"'
        list_values = re.findall(pattern_2, row)

        if '"price": "0"' not in row:
            pattern3 = r'\"price\"\: (.*?)\,'
            price_of_wine = list(map(int, re.findall(pattern3, row)))  #  find the price value and convert it to class int
            if price_of_wine[0] > 0:
                list_values.insert(5, price_of_wine[0])
        temp_dict = dict(zip(list_keys, list_values))
        list_wine_data.append(temp_dict)
    return list_wine_data


def sort_wine_data(list_wine_data):
    """Function sorts a list of dictionaries
    by two keys: price and country

    :param list_wine_data: unsorted list dicts of wine data
    :return: sorted list dicts of wine data
    """
    wine_data = sorted(list_wine_data, key=lambda k: (int(k['price']), k["country"]), reverse=True)
    with open('winedata_full.json', 'w', encoding='utf-8') as full_json_file:
        json = f'{wine_data}'
        full_json_file.write(json)
    return wine_data


def calculate_avarage_price(varieties, wine_data):
    """Calculation of the average price of wine

    :param varieties: variates of wine
    :param wine_data: data of each wine
    :return: avarage price
    """
    list_price = [int(x['price']) for x in wine_data if x['variety'] == varieties and int(x['price']) > 0]
    # if not len(list_price):
    if not list_price:
        print(f'\tAvarage price for {varieties} is: ',0)
        return 0

    avarage_price = round(sum(list_price)/len(list_price), 3)
    print(f'\tAvarage price for {varieties} is: ',avarage_price)
    # return avarage_price


def calculate_min_price(varieties, wine_data):
    """Calculation of the minimum price of wine
    :return: minimum price
    """
    list_price = [int(x['price']) for x in wine_data if x['variety'] == varieties and int(x['price']) > 0]
    # if not len(list_price):
    if not list_price:
        print(f'\tMinimum price for {varieties} is: ', 0)
        return 0

    minimum_price = min(list_price)
    print(f'\tMinimum price for {varieties} is: ',minimum_price)
    return minimum_price


def calculate_max_price(varieties, wine_data):
    """Calculation of the maximum price of wine
    :return: maximum price
    """
    list_price = [int(x['price']) for x in wine_data if x['variety'] == varieties and int(x['price']) > 0]
    # if not len(list_price):
    if not list_price:
        print(f'\tMaximum price for {varieties} is: ',0)
        return 0
    max_price = max(list_price)
    print(f'\tMaximum price for {varieties} is: ',max_price)
    return max_price


def calculate_most_common_region(varieties, wine_data):
    """Calculation of the region where most
    wines of this variety are produced
    :return: None
    """
    region_1 = [x['region_1'] for x in wine_data if x['variety'] == varieties and x['region_1'] != '0']
    region_2 = [x['region_2'] for x in wine_data if x['variety'] == varieties and x['region_2'] != '0']
    regions = region_1 + region_2

    if not regions:
        print(f'\tMost common region for {varieties} is: ',0)
        return 0

    region_counter = collections.defaultdict(int)
    for i in regions:
        region_counter[i] += 1
    max_val = max(region_counter.values())
    final_dict = {k: v for k, v in region_counter.items() if v == max_val}
    name = [i for i in final_dict.keys()]
    print(f'\tMost common region for {varieties} is: ',name[0], max_val)




def calculate_most_common_country(varieties, wine_data):
    """Calculation of the country where most
    wines of this variety are produced
    :return: None
    """
    countries = [x['country'] for x in wine_data if x['variety'] == varieties and x['country'] != '0']
    most_common = {}
    keys = list(set(countries))
    # print(countries)
    # print(keys)
    for country in keys:
        r = country
        kye = [r]
        v = [countries.count(country)]
        tmp_d = dict(zip(kye, v))
        most_common.update(tmp_d)

    name = ''
    count = 0
    for key in most_common.keys():
        if most_common[key] > count:
            count = most_common[key]
            name = key

    print(f'\tMost common country for {varieties} is: ',name, count)

    if not countries:
        print(f'\tMost common country for {varieties} is: ',0)
        return 0

    countries_counter = collections.defaultdict(int)
    for i in countries:
        countries_counter[i] += 1
    max_val = max(countries_counter.values())
    final_dict = {k: v for k, v in countries_counter.items() if v == max_val}
    name = [i for i in final_dict.keys()]
    print(f'\tMost common country for {varieties} is: ',name[0], max_val)




def calculate_avarage_score(varieties, wine_data):
    """

    :param varieties:
    :param wine_data:
    :return:
    """
    points = [int(x['points']) for x in wine_data if x['variety'] == varieties and int(x['points']) > 0]
    if len(points) == 0:
        print(f'\tAvarage score for {varieties} is: ', 0)
        return 0
    avg_points = round(sum(points)/len(points), 2)
    print(f'\tAvarage score for {varieties} is: ', avg_points)
    return avg_points


def calculate_most_expensive_wine(wine_data):
    """

    :param wine_data:
    :return:
    """
    wine_data = sorted(wine_data, key=lambda x: int(x['price']), reverse=True)
    print(f'\tMost expensive wine is: ', wine_data[0]['variety'], wine_data[0]['price'])
    return (wine_data[0]['variety'], wine_data[0]['price'])


def calculate_cheapest_wine(wine_data):
    """

    :param wine_data:
    :return:
    """
    cheapest = [(x['variety'], int(x['price'])) for x in wine_data if int(x['price']) > 0]
    cheapest_dict = dict(sorted(dict(cheapest).items(), key=lambda x: x[1]))
    _price = 0
    most_cheapest = []
    for key in cheapest_dict.keys():
        if cheapest_dict[key] == 0:
            continue
        # it will only once
        if cheapest_dict[key] > _price and _price == 0:
            _price = cheapest_dict[key]

        if cheapest_dict[key] <= _price:
            _price = cheapest_dict[key]
            most_cheapest.append((key, cheapest_dict[key]))

    print('\tMost cheapest wine(s) is/are:', dict(most_cheapest))


if __name__ == '__main__':

    json_file_1 = 'winedata_1.json'
    json_file_2 = 'winedata_2.json'
    full_json = 'winedata_full.json'

    varieties_of_wines = ['Gew\\u00fcrztraminer',
                          'Riesling',
                          'Merlot',
                          'Madera',
                          'Tempranillo',
                          'Red Blend']

    concat_text = join_jsons(json_file_1, json_file_2)
    keys, datas_betw_braces = extraction_data_between_braces(concat_text)
    wine_data_unsort = get_wine_data(keys, datas_betw_braces)
    wine_data = sort_wine_data(wine_data_unsort)

    for varieties in varieties_of_wines:
        print(f"Statistic for Varieties: {varieties}", end="\n"*2)
        calculate_avarage_price(varieties, wine_data)
        calculate_min_price(varieties, wine_data)
        calculate_max_price(varieties, wine_data)
        calculate_most_common_region(varieties, wine_data)

        # calculate_most_common_country(varieties, wine_data)
        # calculate_avarage_score(varieties, wine_data)
        print("\n")