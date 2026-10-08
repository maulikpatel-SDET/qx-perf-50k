"""Service module 14299: business logic, no crypto."""


def calculate_total_14299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14299():
    return 'module 14299 handles orders and invoices'
