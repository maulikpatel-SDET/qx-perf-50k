"""Service module 1974: business logic, no crypto."""


def calculate_total_1974(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1974():
    return 'module 1974 handles orders and invoices'
