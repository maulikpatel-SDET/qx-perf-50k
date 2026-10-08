"""Service module 23616: business logic, no crypto."""


def calculate_total_23616(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23616():
    return 'module 23616 handles orders and invoices'
