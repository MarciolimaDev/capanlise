from rest_framework import serializers
from .models import Sorteio, Premio, Dezena



class DezenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dezena
        fields = ['numero']

class PremioSerializer(serializers.ModelSerializer):
    dezenas = DezenaSerializer(many=True)

    class Meta:
        model = Premio
        fields = ['ordemPremio', 'dezenas']

class SorteioSerializer(serializers.ModelSerializer):
    premios = PremioSerializer(many=True)

    class Meta:
        model = Sorteio
        fields = ['id', 'numeroEdicao', 'anoEdicao', 'dataEdicao', 'premios']
