"""Service module 10694: business logic, no crypto."""


def calculate_total_10694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10694():
    return 'module 10694 handles orders and invoices'
