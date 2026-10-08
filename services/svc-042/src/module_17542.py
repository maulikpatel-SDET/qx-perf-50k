"""Service module 17542: business logic, no crypto."""


def calculate_total_17542(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17542():
    return 'module 17542 handles orders and invoices'
