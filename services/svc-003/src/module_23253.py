"""Service module 23253: business logic, no crypto."""


def calculate_total_23253(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23253():
    return 'module 23253 handles orders and invoices'
