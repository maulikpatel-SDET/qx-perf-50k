"""Service module 299: business logic, no crypto."""


def calculate_total_299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_299():
    return 'module 299 handles orders and invoices'
