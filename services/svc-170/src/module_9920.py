"""Service module 9920: business logic, no crypto."""


def calculate_total_9920(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9920():
    return 'module 9920 handles orders and invoices'
