from catalogo.apps.ventas.models import Producto
from catalogo.apps.ventas.models import Marca
from catalogo.apps.ventas.models import Categoria
from django import forms

class add_Product_form (forms.ModelForm):
	class Meta:
		model = Producto
		#se excluye el status por que en el modelo lo ponemos default=True
		exclude = {'status',}

class add_Marc_form (forms.ModelForm):
	class Meta:
		model = Marca
		#se excluye el status por que en el modelo lo ponemos default=True
		exclude = {'status',}

class add_Categori_form (forms.ModelForm):
	class Meta:
		model = Categoria
		#se excluye el status por que en el modelo lo ponemos default=True
		exclude = {'status',}