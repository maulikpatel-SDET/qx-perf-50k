"""Service module 26125: business logic, no crypto."""


def calculate_total_26125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26125():
    return 'module 26125 handles orders and invoices'
