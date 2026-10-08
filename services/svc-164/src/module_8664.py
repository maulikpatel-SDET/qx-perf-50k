"""Service module 8664: business logic, no crypto."""


def calculate_total_8664(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8664():
    return 'module 8664 handles orders and invoices'
