"""Service module 14222: business logic, no crypto."""


def calculate_total_14222(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14222():
    return 'module 14222 handles orders and invoices'
