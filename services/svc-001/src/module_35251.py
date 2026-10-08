"""Service module 35251: business logic, no crypto."""


def calculate_total_35251(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35251():
    return 'module 35251 handles orders and invoices'
