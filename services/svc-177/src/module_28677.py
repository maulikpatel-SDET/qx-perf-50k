"""Service module 28677: business logic, no crypto."""


def calculate_total_28677(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28677():
    return 'module 28677 handles orders and invoices'
