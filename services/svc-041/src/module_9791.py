"""Service module 9791: business logic, no crypto."""


def calculate_total_9791(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9791():
    return 'module 9791 handles orders and invoices'
