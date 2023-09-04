def monkeypatch() -> None:
    from typing import Any

    import django_stubs_ext
    from celery.app.task import Task

    django_stubs_ext.monkeypatch()
    Task.__class_getitem__ = classmethod(lambda cls, *args, **kwargs: cls)  # type: ignore[attr-defined]

    from django.forms.widgets import Input

    def add_type_to_classes(init_func: Any) -> Any:
        def dec(self: Input, attrs: Any = None) -> Any:
            if self.input_type is not None:
                if attrs is None:
                    attrs = {}

                css_class = f"{self.template_name.split('/')[-1].split('.')[0]}"

                if "class" not in attrs:
                    attrs["class"] = css_class
                else:
                    attrs["class"] += " " + css_class
            init_func(self, attrs)

        return dec

    Input.__init__ = add_type_to_classes(Input.__init__)  # type: ignore[method-assign]
