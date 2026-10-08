"""Service module 14699: business logic, no crypto."""


def calculate_total_14699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14699():
    return 'module 14699 handles orders and invoices'
