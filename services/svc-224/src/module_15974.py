"""Service module 15974: business logic, no crypto."""


def calculate_total_15974(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15974():
    return 'module 15974 handles orders and invoices'
