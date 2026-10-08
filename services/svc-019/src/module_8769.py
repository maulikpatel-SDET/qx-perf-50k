"""Service module 8769: business logic, no crypto."""


def calculate_total_8769(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8769():
    return 'module 8769 handles orders and invoices'
