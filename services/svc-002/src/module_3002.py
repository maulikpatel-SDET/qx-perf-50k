"""Service module 3002: business logic, no crypto."""


def calculate_total_3002(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3002():
    return 'module 3002 handles orders and invoices'
