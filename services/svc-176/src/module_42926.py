"""Service module 42926: business logic, no crypto."""


def calculate_total_42926(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42926():
    return 'module 42926 handles orders and invoices'
