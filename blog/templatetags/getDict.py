from django import template

register = template.Library()

@register.filter(name="get_Dict")
def get_Dict(dict,key):
    return dict.get(key)


   
