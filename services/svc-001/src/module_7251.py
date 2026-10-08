"""Service module 7251: business logic, no crypto."""


def calculate_total_7251(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7251():
    return 'module 7251 handles orders and invoices'
