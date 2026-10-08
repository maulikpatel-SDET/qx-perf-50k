"""Service module 17664: business logic, no crypto."""


def calculate_total_17664(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17664():
    return 'module 17664 handles orders and invoices'
