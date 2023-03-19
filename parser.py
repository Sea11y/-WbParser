import time
import chromedriver_binary
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from wordCsv import full_articles, rit, rerit

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox(84.0)")
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

articles_list = []
brand_list = []
sale_size_list = []
price_with_sale_list = []
price_spp_list = []
size_spp_list = []
name_list = []
url_list = []
have_list = []
rating_list = []
count_featback_list = []
count_buy_list = []

for_time_hours = input('Введите кол-во часов для периода парсинга: ')
for_time_minut = input('Введите кол-во минут для периода парсинга: ')

def get_info():
    rerit()
    try:
        for i in range(0, len(full_articles)):
            url = f'https://www.wildberries.ru/catalog/{full_articles[i]}/detail.aspx?targetUrl=SP'
            driver.get(url=url)
            time.sleep(4)
            try:
                anyway = driver.find_element(By.XPATH, "//h1[@class='content404__title']")
                have_list.append('По запросу ничего не найдено')
                articles_list.append(0)
                brand_list.append(0)
                sale_size_list.append(0)
                price_with_sale_list.append(0)
                price_spp_list.append(0)
                size_spp_list.append(0)
                name_list.append(0)
                url_list.append(url)
                rating_list.append(0)
                count_featback_list.append(0)
                count_buy_list.append(0)
            except:
                try:
                    not_have = driver.find_element(By.XPATH, "//span[@class='sold-out-product__text']")
                    have_list.append('Нет в наличии')
                    articles_list.append(0)
                    brand_list.append(0)
                    sale_size_list.append(0)
                    price_with_sale_list.append(0)
                    price_spp_list.append(0)
                    size_spp_list.append(0)
                    name_list.append(0)
                    url_list.append(url)
                    rating_list.append(0)
                    count_featback_list.append(0)
                    count_buy_list.append(0)

                except:
                    driver.execute_script("window.scrollTo(0, 1500)")
                    time.sleep(4)
                    get_price = driver.find_element(By.XPATH, "//ins[@class='price-block__final-price']")
                    get_price_without_sale = driver.find_element(By.XPATH, "//del")
                    # Основная цена товара
                    numbera = get_price.text.split(' ₽')[0]
                    # Цена без скидки
                    numberb = get_price_without_sale.text.split(' ₽')[0]
                    # Размер скидки
                    b = numberb.split(' ')
                    a = numbera.split(' ')
                    main_price_without_sale = int(''.join(map(str, b)))
                    main_price = int(''.join(map(str, a)))
                    # Бренд
                    sale_size = main_price_without_sale - main_price
                    get_brand = driver.find_element(By.XPATH, "//a[@class ='seller-info__name seller-info__name--link']").text
                    # Имя Товара
                    product_name = driver.find_element(By.XPATH, "//h1").text
                    # Кол-во отзывов
                    count_featback = driver.find_element(By.XPATH, "//span[@class='user-activity__count']").text
                    # Рейтинг
                    first_rating = driver.find_element(By.XPATH, "//b[@class='user-opinion__rating-numb']").text
                    try:
                        rating = first_rating.replace('.', ',', 1)
                    except:
                        rating = first_rating
                    # Кол-во Покупок
                    count_buy = driver.find_element(By.XPATH, "//p[@class='product-order-quantity j-orders-count-wrapper']//span").text
                    # Рассчет СПП от изначальной стоимости товара
                    MAIN_PRICE_PROCENT = sale_size / int(main_price_without_sale) * 100
                    SPP = int(int(main_price_without_sale) * (100-MAIN_PRICE_PROCENT)/100)
                    # Размер СПП
                    SPP_SIZE = int(main_price_without_sale) - SPP

                    have_list.append(1)
                    articles_list.append(full_articles[i])
                    brand_list.append(get_brand)
                    sale_size_list.append(sale_size)
                    price_with_sale_list.append(main_price)
                    price_spp_list.append(SPP)
                    size_spp_list.append(SPP_SIZE)
                    name_list.append(product_name)
                    url_list.append(url)
                    rating_list.append(rating)
                    count_featback_list.append(count_featback)
                    count_buy_list.append(count_buy)

            print(f'Спарсилось {i + 1} из {len(full_articles)}')

            rit(articles_list[i], brand_list[i], sale_size_list[i], price_with_sale_list[i], price_spp_list[i], size_spp_list[i], name_list[i], url_list[i], have_list[i], rating_list[i], count_featback_list[i], count_buy_list[i])
        time.sleep((int(for_time_hours) * 3600) + (int(for_time_minut) * 60))
        get_info()
    except Exception as ex:
        print(ex)
def main():
    get_info()


if __name__ == '__main__':
    main()

