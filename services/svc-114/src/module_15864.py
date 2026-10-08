"""Service module 15864: business logic, no crypto."""


def calculate_total_15864(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15864():
    return 'module 15864 handles orders and invoices'
