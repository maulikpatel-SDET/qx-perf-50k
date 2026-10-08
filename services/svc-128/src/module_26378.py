"""Service module 26378: business logic, no crypto."""


def calculate_total_26378(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26378():
    return 'module 26378 handles orders and invoices'
