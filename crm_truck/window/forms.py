from django import forms

from fleet.models import FilterLabel


class IndexForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(IndexForm, self).__init__(*args, **kwargs)

        filter_list: list[FilterLabel] = FilterLabel.objects.filter(
            active=True, position=0
        )
        for field in filter_list:
            self.fields[field.label] = forms.CharField(max_length=200)
            self.fields[field.label].widget.attrs.update({"class": field.input_classes})
            self.fields[field.label].label_classes = "idk"
