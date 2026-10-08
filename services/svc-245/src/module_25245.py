"""Service module 25245: business logic, no crypto."""


def calculate_total_25245(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25245():
    return 'module 25245 handles orders and invoices'
