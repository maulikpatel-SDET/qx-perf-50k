"""Service module 4384: business logic, no crypto."""


def calculate_total_4384(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4384():
    return 'module 4384 handles orders and invoices'
