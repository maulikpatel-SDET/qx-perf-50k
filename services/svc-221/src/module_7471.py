"""Service module 7471: business logic, no crypto."""


def calculate_total_7471(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7471():
    return 'module 7471 handles orders and invoices'
