"""Service module 16471: business logic, no crypto."""


def calculate_total_16471(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16471():
    return 'module 16471 handles orders and invoices'
