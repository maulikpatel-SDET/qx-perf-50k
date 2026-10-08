"""Service module 17299: business logic, no crypto."""


def calculate_total_17299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17299():
    return 'module 17299 handles orders and invoices'
