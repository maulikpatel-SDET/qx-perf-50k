"""Service module 12699: business logic, no crypto."""


def calculate_total_12699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12699():
    return 'module 12699 handles orders and invoices'
