"""Service module 39173: business logic, no crypto."""


def calculate_total_39173(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39173():
    return 'module 39173 handles orders and invoices'
