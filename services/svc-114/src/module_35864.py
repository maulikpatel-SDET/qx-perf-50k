"""Service module 35864: business logic, no crypto."""


def calculate_total_35864(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35864():
    return 'module 35864 handles orders and invoices'
