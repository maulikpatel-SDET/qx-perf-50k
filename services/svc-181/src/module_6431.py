"""Service module 6431: business logic, no crypto."""


def calculate_total_6431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6431():
    return 'module 6431 handles orders and invoices'
