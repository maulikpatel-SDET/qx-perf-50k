"""Service module 3664: business logic, no crypto."""


def calculate_total_3664(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3664():
    return 'module 3664 handles orders and invoices'
