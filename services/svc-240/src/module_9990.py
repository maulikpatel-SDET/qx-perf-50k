"""Service module 9990: business logic, no crypto."""


def calculate_total_9990(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9990():
    return 'module 9990 handles orders and invoices'
