import scrapy
from scrapy.http import Response


class FullmenuSpider(scrapy.Spider):
    name = "fullmenu"
    allowed_domains = ["www.mcdonalds.com"]
    start_urls = ["https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html"]

    def parse(self, response: Response, **kwargs):
        for product in response.css(".cmp-category__item-link::attr(href)").getall():
            yield response.follow(product, callback=self.parse_product)

    def parse_product(self, response: Response):
        id = response.url.split("/")[-1].replace(".html", "")

        url = f"https://www.mcdonalds.com/dnaapp/itemDetails?country=UA&language=uk&showLiveData=true&item={id}"

        yield scrapy.Request(url, callback=self.parse_product_detail)


    def parse_product_detail(self, response: Response):
        data = response.json()
        item = data.get("item")
        name = item.get("item_name").replace("\"", "")
        description = item.get("description").replace("\r\n", " ")
        nutrient_facts = item.get("nutrient_facts")

        nutrient_map = {
            "Калорійність": "calories",
            "Жири": "fats",
            "НЖК": "unsaturated_fats",
            "Вуглеводи": "carbs",
            "Цукор": "sugar",
            "Білки": "protein",
            "Вага порції": "portion",
            "Сіль": "salt"
        }

        product_details = {
            "name": name,
            "description": description,
            "calories": None,
            "fats": None,
            "carbs": None,
            "protein": None,
            "unsaturated_fats": None,
            "sugar": None,
            "salt": None,
            "portion": None,
        }

        for nutrient_fact in nutrient_facts.get("nutrient"):
            nutrient_name = nutrient_fact.get("name")
            if nutrient_name in nutrient_map:
                product_details[nutrient_map[nutrient_name]] = nutrient_fact.get("value")

        yield product_details
