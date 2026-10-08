"""Service module 42002: business logic, no crypto."""


def calculate_total_42002(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42002():
    return 'module 42002 handles orders and invoices'
