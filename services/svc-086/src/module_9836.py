"""Service module 9836: business logic, no crypto."""


def calculate_total_9836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9836():
    return 'module 9836 handles orders and invoices'
