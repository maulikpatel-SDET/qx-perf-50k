"""Service module 28699: business logic, no crypto."""


def calculate_total_28699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28699():
    return 'module 28699 handles orders and invoices'
