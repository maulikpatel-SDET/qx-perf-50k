"""Service module 8616: business logic, no crypto."""


def calculate_total_8616(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8616():
    return 'module 8616 handles orders and invoices'
