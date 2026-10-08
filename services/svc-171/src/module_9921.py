"""Service module 9921: business logic, no crypto."""


def calculate_total_9921(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9921():
    return 'module 9921 handles orders and invoices'
