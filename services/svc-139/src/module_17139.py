"""Service module 17139: business logic, no crypto."""


def calculate_total_17139(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17139():
    return 'module 17139 handles orders and invoices'
