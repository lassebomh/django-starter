from typing import Any

from django import template

register = template.Library()


@register.inclusion_tag("partials/field.html", takes_context=True)
def field(context: Any, **kwargs) -> Any:
    input_attrs = kwargs

    label_attrs = {
        "for": input_attrs.get("id"),
        "for": input_attrs.pop("label"),
    }

    return {
        "name": "name",
        "label": "label",
        "type": type,
        "errors": context["unicorn"]["errors"].get("name", []),
    }
