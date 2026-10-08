"""Service module 29616: business logic, no crypto."""


def calculate_total_29616(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29616():
    return 'module 29616 handles orders and invoices'
