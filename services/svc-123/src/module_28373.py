"""Service module 28373: business logic, no crypto."""


def calculate_total_28373(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28373():
    return 'module 28373 handles orders and invoices'
