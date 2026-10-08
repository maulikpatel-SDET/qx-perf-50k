"""Service module 41995: business logic, no crypto."""


def calculate_total_41995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41995():
    return 'module 41995 handles orders and invoices'
