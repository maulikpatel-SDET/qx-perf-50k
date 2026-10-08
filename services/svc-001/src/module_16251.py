"""Service module 16251: business logic, no crypto."""


def calculate_total_16251(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16251():
    return 'module 16251 handles orders and invoices'
