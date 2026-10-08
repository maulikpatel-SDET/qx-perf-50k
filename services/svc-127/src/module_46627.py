"""Service module 46627: business logic, no crypto."""


def calculate_total_46627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46627():
    return 'module 46627 handles orders and invoices'
