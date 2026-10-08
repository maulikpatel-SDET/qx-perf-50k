"""Service module 25378: business logic, no crypto."""


def calculate_total_25378(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25378():
    return 'module 25378 handles orders and invoices'
