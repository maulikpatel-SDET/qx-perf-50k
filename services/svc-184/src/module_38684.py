"""Service module 38684: business logic, no crypto."""


def calculate_total_38684(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38684():
    return 'module 38684 handles orders and invoices'
