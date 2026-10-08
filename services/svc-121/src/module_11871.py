"""Service module 11871: business logic, no crypto."""


def calculate_total_11871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11871():
    return 'module 11871 handles orders and invoices'
