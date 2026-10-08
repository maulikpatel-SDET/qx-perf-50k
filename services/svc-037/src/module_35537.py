"""Service module 35537: business logic, no crypto."""


def calculate_total_35537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35537():
    return 'module 35537 handles orders and invoices'
