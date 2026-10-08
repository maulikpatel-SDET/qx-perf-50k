"""Service module 36471: business logic, no crypto."""


def calculate_total_36471(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36471():
    return 'module 36471 handles orders and invoices'
