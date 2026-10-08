"""Service module 6694: business logic, no crypto."""


def calculate_total_6694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6694():
    return 'module 6694 handles orders and invoices'
