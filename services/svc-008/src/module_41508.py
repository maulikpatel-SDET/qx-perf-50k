"""Service module 41508: business logic, no crypto."""


def calculate_total_41508(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41508():
    return 'module 41508 handles orders and invoices'
