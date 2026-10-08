"""Service module 1002: business logic, no crypto."""


def calculate_total_1002(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1002():
    return 'module 1002 handles orders and invoices'
