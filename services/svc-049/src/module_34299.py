"""Service module 34299: business logic, no crypto."""


def calculate_total_34299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34299():
    return 'module 34299 handles orders and invoices'
