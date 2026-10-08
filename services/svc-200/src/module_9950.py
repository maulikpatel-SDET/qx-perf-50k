"""Service module 9950: business logic, no crypto."""


def calculate_total_9950(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9950():
    return 'module 9950 handles orders and invoices'
