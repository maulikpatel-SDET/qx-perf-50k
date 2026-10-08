"""Service module 19694: business logic, no crypto."""


def calculate_total_19694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19694():
    return 'module 19694 handles orders and invoices'
