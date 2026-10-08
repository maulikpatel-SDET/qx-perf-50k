"""Service module 1841: business logic, no crypto."""


def calculate_total_1841(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1841():
    return 'module 1841 handles orders and invoices'
