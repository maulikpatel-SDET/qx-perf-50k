"""Service module 16213: business logic, no crypto."""


def calculate_total_16213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16213():
    return 'module 16213 handles orders and invoices'
