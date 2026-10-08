"""Service module 12031: business logic, no crypto."""


def calculate_total_12031(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12031():
    return 'module 12031 handles orders and invoices'
