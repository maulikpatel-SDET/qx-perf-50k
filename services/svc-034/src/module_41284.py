"""Service module 41284: business logic, no crypto."""


def calculate_total_41284(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41284():
    return 'module 41284 handles orders and invoices'
