"""Service module 45694: business logic, no crypto."""


def calculate_total_45694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45694():
    return 'module 45694 handles orders and invoices'
