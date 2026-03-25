from django import forms


class BootstrapModelForm(forms.ModelForm):
    """Asigna clases Bootstrap 5 a los widgets de ModelForm."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            w = field.widget
            if isinstance(w, forms.HiddenInput):
                continue
            if isinstance(w, forms.CheckboxInput):
                w.attrs.setdefault("class", "form-check-input")
            elif isinstance(w, forms.Textarea):
                w.attrs.setdefault("class", "form-control")
            elif isinstance(
                w,
                (
                    forms.TextInput,
                    forms.EmailInput,
                    forms.NumberInput,
                    forms.PasswordInput,
                ),
            ):
                w.attrs.setdefault("class", "form-control")
            elif isinstance(w, (forms.Select, forms.SelectMultiple)):
                w.attrs.setdefault("class", "form-select")
