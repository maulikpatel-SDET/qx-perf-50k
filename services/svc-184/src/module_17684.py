"""Service module 17684: business logic, no crypto."""


def calculate_total_17684(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17684():
    return 'module 17684 handles orders and invoices'
