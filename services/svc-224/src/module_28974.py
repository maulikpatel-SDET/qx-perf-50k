"""Service module 28974: business logic, no crypto."""


def calculate_total_28974(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28974():
    return 'module 28974 handles orders and invoices'
