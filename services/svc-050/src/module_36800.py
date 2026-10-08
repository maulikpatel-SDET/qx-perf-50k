"""Service module 36800: business logic, no crypto."""


def calculate_total_36800(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36800():
    return 'module 36800 handles orders and invoices'
