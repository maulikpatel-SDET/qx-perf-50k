"""Service module 13694: business logic, no crypto."""


def calculate_total_13694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13694():
    return 'module 13694 handles orders and invoices'
