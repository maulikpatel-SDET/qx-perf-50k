"""Service module 31694: business logic, no crypto."""


def calculate_total_31694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31694():
    return 'module 31694 handles orders and invoices'
