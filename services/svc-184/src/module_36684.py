"""Service module 36684: business logic, no crypto."""


def calculate_total_36684(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36684():
    return 'module 36684 handles orders and invoices'
