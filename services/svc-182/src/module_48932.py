"""Service module 48932: business logic, no crypto."""


def calculate_total_48932(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48932():
    return 'module 48932 handles orders and invoices'
