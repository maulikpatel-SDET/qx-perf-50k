"""Service module 31299: business logic, no crypto."""


def calculate_total_31299(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31299():
    return 'module 31299 handles orders and invoices'
