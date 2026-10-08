"""Service module 14315: business logic, no crypto."""


def calculate_total_14315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14315():
    return 'module 14315 handles orders and invoices'
