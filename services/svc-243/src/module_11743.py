"""Service module 11743: business logic, no crypto."""


def calculate_total_11743(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11743():
    return 'module 11743 handles orders and invoices'
