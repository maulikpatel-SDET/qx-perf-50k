"""Service module 20542: business logic, no crypto."""


def calculate_total_20542(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20542():
    return 'module 20542 handles orders and invoices'
