import factory

from api_app.models import Value, Principle

class ValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Value
    text = factory.Sequence(lambda n: "Value {}".format(n+1))

class PrincipleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Principle
    text = factory.Sequence(lambda n: "Principle {}".format(n+1))
