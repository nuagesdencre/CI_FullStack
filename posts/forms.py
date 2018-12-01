from django import forms

from posts import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("content", "topic")
        model = models.Post

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["topic"].queryset = (
                models.Topic.objects.filter(
                    pk__in=user.topics.values_list("topic__pk")
                )
            )
