"""Service module 25632: business logic, no crypto."""


def calculate_total_25632(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25632():
    return 'module 25632 handles orders and invoices'
