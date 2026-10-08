"""Service module 18256: business logic, no crypto."""


def calculate_total_18256(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18256():
    return 'module 18256 handles orders and invoices'
