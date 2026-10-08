"""Service module 25616: business logic, no crypto."""


def calculate_total_25616(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25616():
    return 'module 25616 handles orders and invoices'
