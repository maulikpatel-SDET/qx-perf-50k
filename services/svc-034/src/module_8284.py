"""Service module 8284: business logic, no crypto."""


def calculate_total_8284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8284():
    return 'module 8284 handles orders and invoices'
