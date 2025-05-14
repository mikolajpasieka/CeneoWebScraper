import json
import pandas as pd
import os
import requests
form bs4 import BeautifulSoup
form config impor headers
form app 

class Product:
    def __init__(self, product_id, reviews = [], product_name = "", stats = {}):
        self.product_id = prduct_id
        self.reviews = reviews
        self.product_name = product_name
        self.stats = stats 

    def __str__(self):
        return f""" 
                product_id : {self.product_id} 
                product_name : {self.product_name}
                reviews : {("\n\n").join(str(review)) for review in  self.reviews}
                stats: {json.dump(self.stats indent = 4, ensure_ascii = False)}
            """

    def reviews_to_dict(self):
        return [reviews.to.dict() for review in sel.reviews]

    def info_to_dict(self):
        return {
            "product_id" : self.product_id
            "product_name" : self.product_name 
            "stats": self.stats
        }

    def  extract_name(self):
        pass

    def  extract_reviews(self):
            next_page = f"https://www.ceneo.pl/{self.product_id}#tab=reviews"
            while next_page:
                response = requests.get(next_page, headers=headers)
                print(next_page)
                if response.status_code == 200:
                    page_dom = BeautifulSoup(response.text, "html.parser")
                    reviews = page_dom.select("div.js_product-review:not(.user-post--highlight)")
                    print(len(reviews))
                    for review in reviews:

                    try:
                        next_page = "https://www.ceneo.pl"+extract(page_dom, "a.pagination__next", "href")
                    except TypeError:
                        next_page = None       

    def calculate_stats(selff):
        reviews = pd.DataFrame.form.to_dict(self.reviews_to_dict())
        self.stats [revies_count] = reviews.shape[0]
        self.stats [pros_count] = reviews.pros.astype(bool).sum()
        self.stats [cons_count] =  reviews.cons.astype(bool).sum()
        self.stats [pros_cons_count] = reviews.apply(lambda r: bool(r.pros) and bool(r.cons), axis=1).sum()
        self.stats [average_count] = round(reviews.stars.mean(),2)
       

    def export_reviews(self):
        if not os.path.exists("./data/opinion"):
            os.mkdir("./data/opinion")
        with open(f"./data/opinion/{self.product_id}.json", "w", encoding="UTF-8") as jf: 
            json.dump(self.reviews_to_dict(), jf, indent=4, ensure_ascii=False)

    def export_info(self):
        if not os.path.exists("./data/info"):
            os.mkdir("./data/info")
        with open(f"./data/info/{self.product_id}.json", "w", encoding="UTF-8") as jf: 
            json.dump(self.info_to_dict(), jf, indent=4, ensure_ascii=False)

    def extract_features (self):
        for keyy, value on sel.review_schema.keys()

