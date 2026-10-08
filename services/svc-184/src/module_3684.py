"""Service module 3684: business logic, no crypto."""


def calculate_total_3684(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3684():
    return 'module 3684 handles orders and invoices'
