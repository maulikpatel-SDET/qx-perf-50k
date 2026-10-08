"""Service module 17616: business logic, no crypto."""


def calculate_total_17616(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17616():
    return 'module 17616 handles orders and invoices'
