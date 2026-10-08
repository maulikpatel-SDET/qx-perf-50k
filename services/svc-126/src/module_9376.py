"""Service module 9376: business logic, no crypto."""


def calculate_total_9376(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9376():
    return 'module 9376 handles orders and invoices'
