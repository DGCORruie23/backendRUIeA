from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from usuario.models import Usuario, Paises, EstadoFuerza, Frases, Municipios, PuntosInternacion, RescatePunto, ConteoRapidoPunto

class UserGetSerializer(ModelSerializer):
	class Meta:
		model = Usuario
		fields = [
			'nickname',
			'password',
			]

class UserGetSerializerC(ModelSerializer):
	class Meta:
		model = Usuario
		fields = [
			'nickname',
			'nombre',
			'apellido',
			'password',
			'estado',
			'tipo',
			]
		
class PaisesGetSerializer(ModelSerializer):
	class Meta:
		model = Paises
		fields = [
			'nombre_pais',
			'iso3',
			]

class MunicipiosGetSerializer(ModelSerializer):
	class Meta:
		model = Municipios
		fields = [
			'estado',
			'estadoAbr',
			'nomMunicipio',
			]
		
class PuntosInterGetSerializer(ModelSerializer):
	class Meta:
		model = PuntosInternacion
		fields = [
			'nombrePunto',
			'estadoPunto',
			'tipoPunto',
			]
		
		
class FrasesGetSerializer(ModelSerializer):
	class Meta:
		model = Frases
		fields = [
			'quote',
			'author',
			]

class EstadoFuerzaGetSerializer(ModelSerializer):
	class Meta:
		model = EstadoFuerza
		fields = [
			'oficinaR',
			'numPunto',
			'nomPuntoRevision',
			'tipoP',
			'ubicacion',
			'coordenadasTexto',
			'latitud',
			'longitud',
			'personalINM',
			'personalSEDENA',
			'personalMarina',
			'personalGuardiaN',
			'personalOTROS',
			'vehiculos',
			'seccion',
			]
		

class RescatePuntoSerializer(ModelSerializer):
	class Meta:
		model = RescatePunto
		fields = [
			'oficinaRepre',
			'fecha',
			'hora',
			'nombreAgente',

			'aeropuerto',
			'carretero',
			'tipoVehic',
			'lineaAutobus',
			'numeroEcono',
			'placas',

			'vehiculoAseg',
			'casaSeguridad',
			'centralAutobus',
			'ferrocarril',
			'empresa',
			'hotel',
			'nombreHotel',
			'puestosADispo',
			'juezCalif',
			'reclusorio',
			'policiaFede',
			'dif',
			'policiaEsta',
			'policiaMuni',
			'guardiaNaci',
			'fiscalia',
			'otrasAuto',
			'voluntarios',
			'otro',
			'presuntosDelincuentes',
			'numPresuntosDelincuentes',
			'municipio',
			'puntoEstra',

			'nacionalidad',
			'iso3',
			'nombre',
			'apellidos',
			'noIdentidad',
			'parentesco',
			'fechaNacimiento',
			'sexo',
			'embarazo',
			'numFamilia',
			'edad',
			]
	def create(self, validated_data):
		return RescatePunto.objects.create(**validated_data)

class ListRescatePuntoSerializer(serializers.HyperlinkedModelSerializer):
	rescatePunto = RescatePuntoSerializer(many = True)

	class Meta:
		model = RescatePunto

class ConteoRapidoSerializer(ModelSerializer):
	class Meta:
		model = ConteoRapidoPunto
		fields = [
			'oficinaRepre',
			'fecha',
			'hora',
			'nombreAgente',

			'aeropuerto',
			'carretero',
			'tipoVehic',
			'lineaAutobus',
			'numeroEcono',
			'placas',

			'vehiculoAseg',
			'casaSeguridad',
			'centralAutobus',
			'ferrocarril',
			'empresa',
			'hotel',
			'nombreHotel',
			'puestosADispo',
			'juezCalif',
			'reclusorio',
			'policiaFede',
			'dif',
			'policiaEsta',
			'policiaMuni',
			'guardiaNaci',
			'fiscalia',
			'otrasAuto',
			'voluntarios',
			'otro',
			'presuntosDelincuentes',
			'numPresuntosDelincuentes',
			'municipio',
			'puntoEstra',

			'nacionalidad',
			'iso3',
			'AS_hombres',
			'AS_mujeresNoEmb',
			'AS_mujeresEmb',
			'nucleosFamiliares',
			'AA_hombres',
			'AA_mujeresNoEmb',
			'AA_mujeresEmb',
			'NNA_A_hombres',
			'NNA_A_mujeresNoEmb',
			'NNA_A_mujeresEmb',
			'NNA_S_hombres',
			'NNA_S_mujeresNoEmb',
			'NNA_S_mujeresEmb',
			]
	def create(self, validated_data):
		return ConteoRapidoPunto.objects.create(**validated_data)