"""Service module 34249: business logic, no crypto."""


def calculate_total_34249(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34249():
    return 'module 34249 handles orders and invoices'
