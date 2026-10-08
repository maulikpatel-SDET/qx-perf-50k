"""Service module 38090: business logic, no crypto."""


def calculate_total_38090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38090():
    return 'module 38090 handles orders and invoices'
