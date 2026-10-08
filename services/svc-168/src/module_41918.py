"""Service module 41918: business logic, no crypto."""


def calculate_total_41918(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41918():
    return 'module 41918 handles orders and invoices'
