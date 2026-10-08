"""Service module 12576: business logic, no crypto."""


def calculate_total_12576(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12576():
    return 'module 12576 handles orders and invoices'
