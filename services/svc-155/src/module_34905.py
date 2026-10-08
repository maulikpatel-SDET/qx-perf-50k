"""Service module 34905: business logic, no crypto."""


def calculate_total_34905(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34905():
    return 'module 34905 handles orders and invoices'
