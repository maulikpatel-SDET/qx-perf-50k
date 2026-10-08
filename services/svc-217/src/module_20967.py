"""Service module 20967: business logic, no crypto."""


def calculate_total_20967(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20967():
    return 'module 20967 handles orders and invoices'
