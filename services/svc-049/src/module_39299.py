"""Service module 39299: business logic, no crypto."""


def calculate_total_39299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39299():
    return 'module 39299 handles orders and invoices'
