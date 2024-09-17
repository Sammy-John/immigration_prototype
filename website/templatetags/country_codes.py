from django import template
import phonenumbers

register = template.Library()

@register.filter
def get_country_code(country):
    """Get the dialing code for a given country."""
    try:
        example_number = phonenumbers.parse("+", country)
        return f"+{example_number.country_code}"
    except phonenumbers.phonenumberutil.NumberParseException:
        return ""
