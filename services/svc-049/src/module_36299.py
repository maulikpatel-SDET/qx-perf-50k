"""Service module 36299: business logic, no crypto."""


def calculate_total_36299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36299():
    return 'module 36299 handles orders and invoices'
