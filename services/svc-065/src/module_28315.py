"""Service module 28315: business logic, no crypto."""


def calculate_total_28315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28315():
    return 'module 28315 handles orders and invoices'
