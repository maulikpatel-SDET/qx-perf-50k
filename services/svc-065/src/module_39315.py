"""Service module 39315: business logic, no crypto."""


def calculate_total_39315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39315():
    return 'module 39315 handles orders and invoices'
