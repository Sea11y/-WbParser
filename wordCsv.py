import csv
full_articles = []
with open("articles.csv") as r_file:
    file_reader = csv.reader(r_file, delimiter = ";")
    for row in file_reader:
        full_articles.append(row[0])


def rit(articles_list, brand_list, sale_size_list, price_with_sale_list, price_spp_list, size_spp_list, name_list, url_list, have_list, rating_list, count_featback_list, count_buy_list):
    with open("result1.csv", 'a', encoding='cp1251') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow([f"{articles_list}", f"{brand_list}", f"{sale_size_list}", f"{price_with_sale_list}", f"{price_spp_list}", f"{size_spp_list}", f"{name_list}", f"{url_list}", f"{have_list}", f"{rating_list}", f"{count_featback_list}", f"{count_buy_list}"])

def rerit():
    with open("result1.csv", 'w',) as csv_file:
        writer = csv.writer(csv_file, delimiter=';')

