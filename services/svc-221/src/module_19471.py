"""Service module 19471: business logic, no crypto."""


def calculate_total_19471(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19471():
    return 'module 19471 handles orders and invoices'
