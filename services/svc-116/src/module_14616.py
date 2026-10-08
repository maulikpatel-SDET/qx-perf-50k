"""Service module 14616: business logic, no crypto."""


def calculate_total_14616(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14616():
    return 'module 14616 handles orders and invoices'
