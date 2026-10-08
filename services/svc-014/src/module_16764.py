"""Service module 16764: business logic, no crypto."""


def calculate_total_16764(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16764():
    return 'module 16764 handles orders and invoices'
