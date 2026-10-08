"""Service module 21378: business logic, no crypto."""


def calculate_total_21378(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21378():
    return 'module 21378 handles orders and invoices'
