"""Service module 38033: business logic, no crypto."""


def calculate_total_38033(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38033():
    return 'module 38033 handles orders and invoices'
