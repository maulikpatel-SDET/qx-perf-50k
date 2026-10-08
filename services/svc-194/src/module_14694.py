"""Service module 14694: business logic, no crypto."""


def calculate_total_14694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14694():
    return 'module 14694 handles orders and invoices'
