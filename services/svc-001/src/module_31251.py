"""Service module 31251: business logic, no crypto."""


def calculate_total_31251(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31251():
    return 'module 31251 handles orders and invoices'
