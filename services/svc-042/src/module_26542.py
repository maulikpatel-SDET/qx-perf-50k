"""Service module 26542: business logic, no crypto."""


def calculate_total_26542(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26542():
    return 'module 26542 handles orders and invoices'
