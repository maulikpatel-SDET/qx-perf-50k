"""Service module 12251: business logic, no crypto."""


def calculate_total_12251(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12251():
    return 'module 12251 handles orders and invoices'
