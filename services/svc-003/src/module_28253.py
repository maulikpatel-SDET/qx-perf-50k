"""Service module 28253: business logic, no crypto."""


def calculate_total_28253(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28253():
    return 'module 28253 handles orders and invoices'
