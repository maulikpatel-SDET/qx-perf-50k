"""Service module 19684: business logic, no crypto."""


def calculate_total_19684(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19684():
    return 'module 19684 handles orders and invoices'
