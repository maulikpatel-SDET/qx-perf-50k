"""Service module 14192: business logic, no crypto."""


def calculate_total_14192(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14192():
    return 'module 14192 handles orders and invoices'
