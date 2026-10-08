"""Service module 14576: business logic, no crypto."""


def calculate_total_14576(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14576():
    return 'module 14576 handles orders and invoices'
