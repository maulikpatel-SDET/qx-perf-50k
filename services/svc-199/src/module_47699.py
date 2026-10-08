"""Service module 47699: business logic, no crypto."""


def calculate_total_47699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47699():
    return 'module 47699 handles orders and invoices'
