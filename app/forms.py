from wtforms import Form, StringField, SubmitField, validators

class ProductForm(Form):
    product_id = StringField("Identyfikator produktu", 
                                name='product_id', 
                                id='product_id',
                                validators=[
                                    validators.DataRequired(message = "Kod produktu jest wymagany"),
                                    validators.Regexp("^[1-9]*$", message ="Kod produktu może zawierać jedynie cyfry"),
                                    validators.length(min = 5, max=10, message = "kod produktu musi mieć od 5 do 10 cyfr")
                                ])
    submit = SubmitField("Pobierz opinie")