"""Service module 11299: business logic, no crypto."""


def calculate_total_11299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11299():
    return 'module 11299 handles orders and invoices'
