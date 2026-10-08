"""Service module 29699: business logic, no crypto."""


def calculate_total_29699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29699():
    return 'module 29699 handles orders and invoices'
