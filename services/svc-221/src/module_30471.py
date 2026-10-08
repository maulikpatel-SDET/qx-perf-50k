"""Service module 30471: business logic, no crypto."""


def calculate_total_30471(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30471():
    return 'module 30471 handles orders and invoices'
