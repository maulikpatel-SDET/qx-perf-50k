"""Service module 24743: business logic, no crypto."""


def calculate_total_24743(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24743():
    return 'module 24743 handles orders and invoices'
