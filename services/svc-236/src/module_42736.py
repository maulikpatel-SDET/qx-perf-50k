"""Service module 42736: business logic, no crypto."""


def calculate_total_42736(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42736():
    return 'module 42736 handles orders and invoices'
