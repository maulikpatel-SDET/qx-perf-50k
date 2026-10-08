"""Service module 12291: business logic, no crypto."""


def calculate_total_12291(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12291():
    return 'module 12291 handles orders and invoices'
