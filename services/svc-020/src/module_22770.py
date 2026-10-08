"""Service module 22770: business logic, no crypto."""


def calculate_total_22770(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22770():
    return 'module 22770 handles orders and invoices'
