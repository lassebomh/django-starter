from typing import Any

from django import template
from django.template import Context

register = template.Library()


@register.inclusion_tag("partials/input.html", takes_context=True)
def input(context: Context, *args: str, **kwargs: str) -> Context:
    kwargs.update({k: "" for k in args})

    _type = kwargs.get("type", "text")
    name = kwargs.get("name", None)
    help_text = kwargs.get("help_text", None)
    label = kwargs.get("label", None)

    attrs = {}
    model = None
    errors = []

    for k, v in kwargs.items():
        if k.startswith("u_"):
            k = "unicorn:" + k[2:].replace("_", ".")

        if k.startswith("unicorn:model"):
            model = v

        attrs[k] = v

    if model:
        if not name:
            name = model

        unicorn: Any | None = context.get("unicorn")

        if unicorn:
            errors = [e["message"] for e in unicorn["errors"].get(model, [])]

    if not label and name:
        label = name.replace("_", " ").title()

    return Context(
        {
            "errors": errors,
            "type": _type,
            "label": label,
            "help_text": help_text,
            "name": name,
            "attrs": attrs.items(),
        }
    )
