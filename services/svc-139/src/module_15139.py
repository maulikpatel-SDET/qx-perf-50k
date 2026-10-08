"""Service module 15139: business logic, no crypto."""


def calculate_total_15139(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15139():
    return 'module 15139 handles orders and invoices'
