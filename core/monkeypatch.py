def monkeypatch() -> None:
    from typing import Any

    import django_stubs_ext
    from celery.app.task import Task

    django_stubs_ext.monkeypatch()
    Task.__class_getitem__ = classmethod(lambda cls, *args, **kwargs: cls)  # type: ignore[attr-defined]

    from django.forms.widgets import Widget

    def add_type_to_classes(init_func: Any) -> Any:
        def dec(self: Any, attrs: Any = None) -> Any:
            if attrs is None:
                attrs = {}

            css_class = getattr(type(self), "css_class", self.template_name.split("/")[-1].split(".")[0])

            if "class" not in attrs:
                attrs["class"] = css_class
            else:
                attrs["class"] += " " + css_class

            init_func(self, attrs)

        return dec

    Widget.__init__ = add_type_to_classes(Widget.__init__)  # type: ignore[method-assign]

    from django.forms import BaseForm, DateInput, DateTimeInput, Form, TimeInput

    DateInput.css_class = "date"  # type: ignore[attr-defined]
    DateInput.input_type = "date"  # type: ignore[attr-defined]
    TimeInput.css_class = "time"  # type: ignore[attr-defined]
    TimeInput.input_type = "time"  # type: ignore[attr-defined]
    DateTimeInput.css_class = "datetime-local"  # type: ignore[attr-defined]
    DateTimeInput.input_type = "datetime-local"  # type: ignore[attr-defined]

    def remove_form_label_suffix(init_func: Any) -> Any:
        def dec(self: BaseForm, *args: Any, **kwargs: Any) -> Any:
            init_func(self, *args, **kwargs)
            self.label_suffix = ""

        return dec

    BaseForm.__init__ = remove_form_label_suffix(BaseForm.__init__)  # type: ignore[method-assign]
    Form.__init__ = remove_form_label_suffix(Form.__init__)  # type: ignore[method-assign]
