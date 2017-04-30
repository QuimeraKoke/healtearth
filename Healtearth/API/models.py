from django.db import models

# Create your models here.
class Food(models.Model):
	name = models.CharField(max_length=20)
	amount = models.DecimalField(max_digits=7, decimal_places=2)
	unit = models.CharField(max_length=10)
	air_pollution = models.DecimalField(max_digits=10, decimal_places=2)
	water_pollution = models.DecimalField(max_digits=10, decimal_places=2)
	garbage = models.DecimalField(max_digits=10, decimal_places=2)
	grade = models.CharField(max_length=1)
	alternatives = models.ManyToManyField("self")

	@staticmethod
	def search(text):
		filtered = Food.objects.filter(name__startswith=text)
		return filtered

	def dict_rep(self):
		return {
			'name' : self.name,
			'label' : str(self.amount) + " " + self.unit,
			'air' : self.air_pollution,
			'water' : self.water_pollution,
			'garbage' : self.garbage,
			'grade' : self.grade,
		}