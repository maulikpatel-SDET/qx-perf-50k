"""Service module 26694: business logic, no crypto."""


def calculate_total_26694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26694():
    return 'module 26694 handles orders and invoices'
