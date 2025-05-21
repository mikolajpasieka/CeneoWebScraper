from wtforms import form, StringField, SubmitField, validators

class ProductForm(form):
    def __init__(self):
        product_id = StringField("Identyfikator produktu",
                                 name = "product_id",
                                 id = "product id",
                                 validator = validators.data_required(),
                                 
                                 )
        submit = SubmitField("Pobierz dane")