"""Service module 13684: business logic, no crypto."""


def calculate_total_13684(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13684():
    return 'module 13684 handles orders and invoices'
