"""Service module 42471: business logic, no crypto."""


def calculate_total_42471(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42471():
    return 'module 42471 handles orders and invoices'
