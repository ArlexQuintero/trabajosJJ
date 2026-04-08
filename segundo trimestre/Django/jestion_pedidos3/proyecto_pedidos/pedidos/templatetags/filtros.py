from django import template

register = template.Library()

@register.filter
def precio_formato(valor):
    try:
        valor      = float(valor)
        entero     = int(valor)
        decimales  = round((valor - entero) * 100)
        entero_fmt = f"{entero:,}".replace(',', '.')
        return f"${entero_fmt},{decimales:02d}"
    except (ValueError, TypeError):
        return f"${valor}"