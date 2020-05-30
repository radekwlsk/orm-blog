from django.conf import settings

import factory


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: f"user-{n}")
    email = factory.Sequence(lambda n: f"user-{n}@example.com")

    class Meta:
        model = settings.AUTH_USER_MODEL
        django_get_or_create = ("username",)

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        if extracted:
            self.set_password(extracted)
        else:
            self.set_password("password")
