import collections
import re


def join_jsons(json_f_1, json_f_2):
    """Opens files, reads, removes, them and
    combines it all in one line, and then write
    to a new full json file

    :param file1: 'winedata_1.json'
    :param file2: 'winedata_2.json'
    :return: concatinated text from two files
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
    """
    list_price = [int(x['price']) for x in wine_data if x['variety'] == varieties and int(x['price']) > 0]
    # if not len(list_price):
    if not list_price:
        print(f'\tAvarage price for {varieties} is: ',0)
        return 0

    avarage_price = round(sum(list_price)/len(list_price), 3)
    print(f'\tAvarage price for {varieties} is: ', avarage_price)
    return avarage_price


def calculate_min_price(varieties, wine_data):
    """Calculation of the minimum price of wine
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
    """
    list_price = [int(x['price']) for x in wine_data if x['variety'] == varieties and int(x['price']) > 0]
    # if not len(list_price):
    if not list_price:
        print(f'\tMaximum price for {varieties} is: ',0)
        return 0
    max_price = max(list_price)
    print(f'\tMaximum price for {varieties} is: ', max_price)
    return max_price


def calculate_most_common_region(varieties, wine_data):
    """Calculation of the region where most
    wines of this variety are produced
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
    print(f'\tMost common region for {varieties} is: ', name[0], max_val)
    return name[0], max_val




def calculate_most_common_country(varieties, wine_data):
    """Calculation of the country where most
    wines of this variety are produced
    """
    countries = [x['country'] for x in wine_data if x['variety'] == varieties and x['country'] != '0']

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
    return name[0], max_val


def calculate_avarage_score(varieties, wine_data):
    """Calculate avarage score for points
    """
    points = [int(x['points']) for x in wine_data if x['variety'] == varieties and int(x['points']) > 0]
    if not points:
        print(f'\tAvarage score for {varieties} is: ', 0)
        return 0
    avarage_points = round(sum(points)/len(points), 2)
    print(f'\tAvarage score for {varieties} is: ', avarage_points, end="\n"*2)
    return avarage_points


def calculate_most_expensive_wine(wine_data):
    """Calculate most expensive wine
    :return: tuple (name of wine, price)
    """
    wine_data = sorted(wine_data, key=lambda k: int(k['price']), reverse=True)
    print(f'\tMost expensive wine is: ', wine_data[0]['variety'], wine_data[0]['price'])
    return wine_data[0]['variety'], wine_data[0]['price']


def calculate_cheapest_wine(wine_data):
    """Calculate most cheapest wine among
    countries
    :return: tuple (name of wine, price)
    """
    cheapest = [(x['variety'], int(x['price'])) for x in wine_data if int(x['price']) > 0]
    d_cheapest = dict(cheapest)
    for k, v in d_cheapest.items():
        if v == 0:
            del d_cheapest[k]
    sort_cheapest = sorted(d_cheapest.items(), key=lambda  k: k[1])
    print("\tMost cheapest wine is: ", sort_cheapest[0][0], sort_cheapest[0][1])
    return sort_cheapest[0][0], sort_cheapest[0][1]


def calculate_highest_score(wine_data):
    """Calculate most highest score
    :return: str "score"
    """
    highest_score = max([int(data["points"]) for data in wine_data])
    print("\tHighest score is: ", highest_score)
    return highest_score


def calculate_lowest_score(wine_data):
    """Calculate most lowest score
    :return: str "score"
    """
    lowest_score = min([int(i['points']) for i in wine_data])
    print("\tLowest score is: ", lowest_score)
    return lowest_score


def calculate_most_rated_country(wine_data):
    """Calculate most rated country
    :return: tuple (name of the country, points)
    """
    rated = [(x['country'], (x['points'])) for x in wine_data if x['country'] != '0' and int(x['points']) > 0]
    d_rated = dict(rated)
    sort_rated = sorted(d_rated.items(), key=lambda k: k[1], reverse=True)
    print("\tMost rated country is: ",sort_rated[0])
    return sort_rated[0]


def calculate_most_active_commentator(wine_data):
    """Caalculate most active commentator
    :return: tuple (Name, count)
    """
    commentator_name = [x["taster_name"] for x in wine_data if x["taster_name"] != '0']
    activity_commentator = collections.defaultdict(int)
    for i in commentator_name:
        activity_commentator[i] += 1
    sorted_list_commentators = sorted(activity_commentator.items(), key=lambda k: k[1], reverse=True)
    print("\tMost active commentator", sorted_list_commentators[0])
    return sorted_list_commentators[0]


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

    with open('mystats.json', 'w') as f:
        print('{"statistics": {', file=f)
        print('\t\t"wine": {', file=f)
        for varieties in varieties_of_wines:

            print(f"\nStatistic for Varieties: {varieties}", end="\n"*2)
            # calculate_avarage_price(varieties, wine_data)
            # calculate_min_price(varieties, wine_data)
            # calculate_max_price(varieties, wine_data)
            # calculate_most_common_region(varieties, wine_data)
            # calculate_most_common_country(varieties, wine_data)
            # calculate_avarage_score(varieties, wine_data)
            # calculate_most_expensive_wine(wine_data)
            # calculate_cheapest_wine(wine_data)
            # calculate_highest_score(wine_data)
            # calculate_lowest_score(wine_data)
            # calculate_most_rated_country(wine_data)
            # calculate_most_active_commentator(wine_data)
            # print("\n")

            print(f'\t\t\t"{varieties}"' + ': {', file=f)

            print('\t\t\t\t"avarege_price":',
                  f'"{calculate_avarage_price(varieties, wine_data)}", ', file=f)

            print('\t\t\t\t"min_price":',
                  f'"{calculate_min_price(varieties, wine_data)}", ', file=f)

            print('\t\t\t\t"max_price":',
                  f'"{calculate_max_price(varieties, wine_data)}", ', file=f)

            print('\t\t\t\t"most_common_region":',
                  f'"{calculate_most_common_region(varieties, wine_data)}", ', file=f)

            print('\t\t\t\t"most_common_country":',
                  f'"{calculate_most_common_country(varieties, wine_data)}", ', file=f)

            print('\t\t\t\t"avarage_score":',
                  f'"{calculate_avarage_score(varieties, wine_data)}"', file=f)
            print('\t\t\t\t},', file=f)
        print("General results:")
        print('\t\t},', file=f)

        print('\t\t"most_expensive_wine":',
              f'"{calculate_most_expensive_wine(wine_data)}",', file=f)

        print('\t\t"cheapest_wine":',
              f'"{calculate_cheapest_wine(wine_data)}",', file=f)

        print('\t\t"highest_score":',
              f'"{calculate_highest_score(wine_data)}",', file=f)

        print('\t\t"lowest_score":',
              f'"{calculate_lowest_score(wine_data)}",', file=f)

        print('\t\t"most_rated_country":',
              f'"{calculate_most_rated_country(wine_data)}",', file=f)

        print('\t\t"most_active_commentator":',
              f'"{calculate_most_active_commentator(wine_data)}",', file=f)
        print('\t\t}', file=f)
        print('}', file=f)