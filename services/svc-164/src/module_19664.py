"""Service module 19664: business logic, no crypto."""


def calculate_total_19664(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19664():
    return 'module 19664 handles orders and invoices'
