"""Service module 49251: business logic, no crypto."""


def calculate_total_49251(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49251():
    return 'module 49251 handles orders and invoices'
