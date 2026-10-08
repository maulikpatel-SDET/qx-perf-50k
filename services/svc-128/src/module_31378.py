"""Service module 31378: business logic, no crypto."""


def calculate_total_31378(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31378():
    return 'module 31378 handles orders and invoices'
