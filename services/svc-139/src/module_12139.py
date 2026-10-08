"""Service module 12139: business logic, no crypto."""


def calculate_total_12139(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12139():
    return 'module 12139 handles orders and invoices'
