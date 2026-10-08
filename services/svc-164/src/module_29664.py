"""Service module 29664: business logic, no crypto."""


def calculate_total_29664(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29664():
    return 'module 29664 handles orders and invoices'
