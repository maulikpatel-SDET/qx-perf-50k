"""Service module 2251: business logic, no crypto."""


def calculate_total_2251(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2251():
    return 'module 2251 handles orders and invoices'
