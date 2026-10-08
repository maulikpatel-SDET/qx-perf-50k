"""Service module 49371: business logic, no crypto."""


def calculate_total_49371(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49371():
    return 'module 49371 handles orders and invoices'
