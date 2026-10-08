"""Service module 24387: business logic, no crypto."""


def calculate_total_24387(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24387():
    return 'module 24387 handles orders and invoices'
