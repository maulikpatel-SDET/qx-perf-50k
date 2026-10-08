"""Service module 37871: business logic, no crypto."""


def calculate_total_37871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37871():
    return 'module 37871 handles orders and invoices'
