"""Service module 25694: business logic, no crypto."""


def calculate_total_25694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25694():
    return 'module 25694 handles orders and invoices'
