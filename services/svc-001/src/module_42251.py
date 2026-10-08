"""Service module 42251: business logic, no crypto."""


def calculate_total_42251(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42251():
    return 'module 42251 handles orders and invoices'
