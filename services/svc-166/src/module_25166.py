"""Service module 25166: business logic, no crypto."""


def calculate_total_25166(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25166():
    return 'module 25166 handles orders and invoices'
