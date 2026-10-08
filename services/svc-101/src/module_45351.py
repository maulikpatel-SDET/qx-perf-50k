"""Service module 45351: business logic, no crypto."""


def calculate_total_45351(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45351():
    return 'module 45351 handles orders and invoices'
