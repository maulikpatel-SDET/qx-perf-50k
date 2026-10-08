"""Service module 3616: business logic, no crypto."""


def calculate_total_3616(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3616():
    return 'module 3616 handles orders and invoices'
