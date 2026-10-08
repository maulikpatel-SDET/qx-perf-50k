"""Service module 18031: business logic, no crypto."""


def calculate_total_18031(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18031():
    return 'module 18031 handles orders and invoices'
