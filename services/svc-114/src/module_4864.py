"""Service module 4864: business logic, no crypto."""


def calculate_total_4864(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4864():
    return 'module 4864 handles orders and invoices'
