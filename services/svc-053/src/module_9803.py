"""Service module 9803: business logic, no crypto."""


def calculate_total_9803(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9803():
    return 'module 9803 handles orders and invoices'
