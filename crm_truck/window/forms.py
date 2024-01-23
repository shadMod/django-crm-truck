from django import forms
from django.template.defaultfilters import mark_safe

from fleet.models import FilterLabel


class IndexForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(IndexForm, self).__init__(*args, **kwargs)

        filter_list: list[FilterLabel] = FilterLabel.objects.filter(
            active=True, position=0
        )
        for field in filter_list:
            data = field.get_data
            if isinstance(data, list):
                choices = tuple()
                for i, val in enumerate(data):
                    t_choice = (i, val,)
                    choices = choices + (t_choice,)
                self.fields[field.label] = forms.ChoiceField(choices=choices)
            elif isinstance(data, int):
                self.fields[field.label] = forms.IntegerField(min_value=field.min_value, max_value=field.max_value)
            else:
                self.fields[field.label] = forms.CharField(max_length=200)
            # set css classes
            label = f"""
            <label for="{field.label}" class="{field.label_classes}">
                {field.title}
            </label>
            """
            self.fields[field.label].label = mark_safe(label)
            self.fields[field.label].widget.attrs.update({"class": field.input_classes})
