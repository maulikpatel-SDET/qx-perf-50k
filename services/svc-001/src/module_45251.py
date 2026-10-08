"""Service module 45251: business logic, no crypto."""


def calculate_total_45251(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45251():
    return 'module 45251 handles orders and invoices'
