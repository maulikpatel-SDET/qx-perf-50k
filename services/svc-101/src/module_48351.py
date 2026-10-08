"""Service module 48351: business logic, no crypto."""


def calculate_total_48351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48351():
    return 'module 48351 handles orders and invoices'
