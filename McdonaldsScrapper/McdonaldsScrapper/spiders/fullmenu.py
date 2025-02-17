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
        name = item.get("item_name")
        description = item.get("description")
        nutrient_facts = item.get("nutrient_facts")

        calories = None
        fats = None
        unsaturated_fats = None
        carbs = None
        sugar = None
        protein = None
        portion = None
        salt = None

        for nutrient_fact in nutrient_facts.get("nutrient"):
            nutrient_name = nutrient_fact.get("name")
            if nutrient_name == "Калорійність":
                calories = nutrient_fact.get("value")
            elif nutrient_name == "Жири":
                fats = nutrient_fact.get("value")
            elif nutrient_name == "НЖК":
                unsaturated_fats = nutrient_fact.get("value")
            elif nutrient_name == "Вуглеводи":
                carbs = nutrient_fact.get("value")
            elif nutrient_name == "Цукор":
                sugar = nutrient_fact.get("value")
            elif nutrient_name == "Білки":
                protein = nutrient_fact.get("value")
            elif nutrient_name == "Вага порції":
                portion = nutrient_fact.get("value")
            elif nutrient_name == "Сіль":
                salt = nutrient_fact.get("value")

        yield {
            "name": name,
            "description": description,
            "calories": calories,
            "fats": fats,
            "carbs": carbs,
            "protein": protein,
            "unsaturated_fats": unsaturated_fats,
            "sugar": sugar,
            "salt": salt,
            "portion": portion,
        }
