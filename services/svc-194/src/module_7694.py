"""Service module 7694: business logic, no crypto."""


def calculate_total_7694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7694():
    return 'module 7694 handles orders and invoices'
