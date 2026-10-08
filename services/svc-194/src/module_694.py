"""Service module 694: business logic, no crypto."""


def calculate_total_694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_694():
    return 'module 694 handles orders and invoices'
