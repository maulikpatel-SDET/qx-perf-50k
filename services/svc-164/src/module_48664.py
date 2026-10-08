"""Service module 48664: business logic, no crypto."""


def calculate_total_48664(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48664():
    return 'module 48664 handles orders and invoices'
