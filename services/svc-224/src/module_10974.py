"""Service module 10974: business logic, no crypto."""


def calculate_total_10974(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10974():
    return 'module 10974 handles orders and invoices'
