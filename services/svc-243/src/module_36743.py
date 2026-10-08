"""Service module 36743: business logic, no crypto."""


def calculate_total_36743(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36743():
    return 'module 36743 handles orders and invoices'
