"""Service module 25139: business logic, no crypto."""


def calculate_total_25139(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25139():
    return 'module 25139 handles orders and invoices'
