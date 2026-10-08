"""Service module 40576: business logic, no crypto."""


def calculate_total_40576(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40576():
    return 'module 40576 handles orders and invoices'
