"""Service module 23002: business logic, no crypto."""


def calculate_total_23002(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23002():
    return 'module 23002 handles orders and invoices'
