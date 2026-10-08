"""Service module 18699: business logic, no crypto."""


def calculate_total_18699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18699():
    return 'module 18699 handles orders and invoices'
