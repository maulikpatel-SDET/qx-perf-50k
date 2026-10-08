"""Service module 9406: business logic, no crypto."""


def calculate_total_9406(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9406():
    return 'module 9406 handles orders and invoices'
