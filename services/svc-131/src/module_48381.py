"""Service module 48381: business logic, no crypto."""


def calculate_total_48381(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48381():
    return 'module 48381 handles orders and invoices'
