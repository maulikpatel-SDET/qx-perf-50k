"""Service module 35378: business logic, no crypto."""


def calculate_total_35378(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35378():
    return 'module 35378 handles orders and invoices'
