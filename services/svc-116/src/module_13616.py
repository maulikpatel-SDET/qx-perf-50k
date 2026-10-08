"""Service module 13616: business logic, no crypto."""


def calculate_total_13616(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13616():
    return 'module 13616 handles orders and invoices'
