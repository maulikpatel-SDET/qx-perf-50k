"""Service module 42315: business logic, no crypto."""


def calculate_total_42315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42315():
    return 'module 42315 handles orders and invoices'
