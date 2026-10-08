"""Service module 31841: business logic, no crypto."""


def calculate_total_31841(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31841():
    return 'module 31841 handles orders and invoices'
