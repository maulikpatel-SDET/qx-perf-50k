"""Service module 15694: business logic, no crypto."""


def calculate_total_15694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15694():
    return 'module 15694 handles orders and invoices'
