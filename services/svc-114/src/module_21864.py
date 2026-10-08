"""Service module 21864: business logic, no crypto."""


def calculate_total_21864(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21864():
    return 'module 21864 handles orders and invoices'
