"""Service module 38139: business logic, no crypto."""


def calculate_total_38139(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38139():
    return 'module 38139 handles orders and invoices'
