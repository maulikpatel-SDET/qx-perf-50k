"""Service module 9876: business logic, no crypto."""


def calculate_total_9876(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9876():
    return 'module 9876 handles orders and invoices'
