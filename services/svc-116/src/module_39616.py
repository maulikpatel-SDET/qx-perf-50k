"""Service module 39616: business logic, no crypto."""


def calculate_total_39616(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39616():
    return 'module 39616 handles orders and invoices'
