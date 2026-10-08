"""Service module 29378: business logic, no crypto."""


def calculate_total_29378(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29378():
    return 'module 29378 handles orders and invoices'
