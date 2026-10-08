"""Service module 11005: business logic, no crypto."""


def calculate_total_11005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11005():
    return 'module 11005 handles orders and invoices'
