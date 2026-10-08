"""Service module 37997: business logic, no crypto."""


def calculate_total_37997(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37997():
    return 'module 37997 handles orders and invoices'
