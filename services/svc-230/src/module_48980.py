"""Service module 48980: business logic, no crypto."""


def calculate_total_48980(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48980():
    return 'module 48980 handles orders and invoices'
