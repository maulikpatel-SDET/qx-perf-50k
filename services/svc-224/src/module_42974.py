"""Service module 42974: business logic, no crypto."""


def calculate_total_42974(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42974():
    return 'module 42974 handles orders and invoices'
