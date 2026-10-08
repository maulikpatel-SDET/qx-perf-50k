"""Service module 20576: business logic, no crypto."""


def calculate_total_20576(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20576():
    return 'module 20576 handles orders and invoices'
