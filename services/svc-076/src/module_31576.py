"""Service module 31576: business logic, no crypto."""


def calculate_total_31576(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31576():
    return 'module 31576 handles orders and invoices'
