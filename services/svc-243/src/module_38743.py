"""Service module 38743: business logic, no crypto."""


def calculate_total_38743(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38743():
    return 'module 38743 handles orders and invoices'
