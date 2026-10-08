"""Service module 41351: business logic, no crypto."""


def calculate_total_41351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41351():
    return 'module 41351 handles orders and invoices'
