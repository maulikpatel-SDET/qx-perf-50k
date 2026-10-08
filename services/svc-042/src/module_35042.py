"""Service module 35042: business logic, no crypto."""


def calculate_total_35042(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35042():
    return 'module 35042 handles orders and invoices'
