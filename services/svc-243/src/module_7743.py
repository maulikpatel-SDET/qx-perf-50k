"""Service module 7743: business logic, no crypto."""


def calculate_total_7743(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7743():
    return 'module 7743 handles orders and invoices'
