"""Service module 2699: business logic, no crypto."""


def calculate_total_2699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2699():
    return 'module 2699 handles orders and invoices'
