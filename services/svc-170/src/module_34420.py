"""Service module 34420: business logic, no crypto."""


def calculate_total_34420(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34420():
    return 'module 34420 handles orders and invoices'
