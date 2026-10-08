"""Service module 8384: business logic, no crypto."""


def calculate_total_8384(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8384():
    return 'module 8384 handles orders and invoices'
