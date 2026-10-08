"""Service module 1031: business logic, no crypto."""


def calculate_total_1031(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1031():
    return 'module 1031 handles orders and invoices'
