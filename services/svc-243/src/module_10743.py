"""Service module 10743: business logic, no crypto."""


def calculate_total_10743(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10743():
    return 'module 10743 handles orders and invoices'
