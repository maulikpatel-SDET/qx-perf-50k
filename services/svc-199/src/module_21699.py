"""Service module 21699: business logic, no crypto."""


def calculate_total_21699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21699():
    return 'module 21699 handles orders and invoices'
