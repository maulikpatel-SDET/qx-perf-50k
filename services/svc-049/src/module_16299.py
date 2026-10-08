"""Service module 16299: business logic, no crypto."""


def calculate_total_16299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16299():
    return 'module 16299 handles orders and invoices'
