"""Service module 41455: business logic, no crypto."""


def calculate_total_41455(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41455():
    return 'module 41455 handles orders and invoices'
