"""Service module 20717: business logic, no crypto."""


def calculate_total_20717(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20717():
    return 'module 20717 handles orders and invoices'
