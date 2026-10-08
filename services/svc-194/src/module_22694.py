"""Service module 22694: business logic, no crypto."""


def calculate_total_22694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22694():
    return 'module 22694 handles orders and invoices'
