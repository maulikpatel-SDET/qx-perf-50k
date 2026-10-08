"""Service module 11004: business logic, no crypto."""


def calculate_total_11004(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11004():
    return 'module 11004 handles orders and invoices'
