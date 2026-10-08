"""Service module 16090: business logic, no crypto."""


def calculate_total_16090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16090():
    return 'module 16090 handles orders and invoices'
