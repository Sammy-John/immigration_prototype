# website/templatetags/country_codes.py

from django import template
from phonenumbers import COUNTRY_CODE_TO_REGION_CODE
import pycountry

register = template.Library()

@register.simple_tag
def get_country_choices():
    """Returns a list of tuples with country codes and names."""
    countries = []
    for code, regions in COUNTRY_CODE_TO_REGION_CODE.items():
        for region in regions:
            try:
                # Use pycountry to get the country name from the region code
                country = pycountry.countries.get(alpha_2=region)
                if country:
                    countries.append((f"+{code}", country.name))
            except KeyError:
                continue

    # Remove duplicates and sort countries alphabetically by name
    countries = list(set(countries))
    countries.sort(key=lambda x: x[1])
    return countries
