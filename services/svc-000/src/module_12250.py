"""Service module 12250: business logic, no crypto."""


def calculate_total_12250(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12250():
    return 'module 12250 handles orders and invoices'
