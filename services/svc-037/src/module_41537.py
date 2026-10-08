"""Service module 41537: business logic, no crypto."""


def calculate_total_41537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41537():
    return 'module 41537 handles orders and invoices'
