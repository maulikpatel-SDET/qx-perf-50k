"""Service module 32022: business logic, no crypto."""


def calculate_total_32022(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32022():
    return 'module 32022 handles orders and invoices'
