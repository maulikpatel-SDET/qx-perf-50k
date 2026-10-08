"""Service module 4213: business logic, no crypto."""


def calculate_total_4213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4213():
    return 'module 4213 handles orders and invoices'
