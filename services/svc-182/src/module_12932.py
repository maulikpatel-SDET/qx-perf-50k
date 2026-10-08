"""Service module 12932: business logic, no crypto."""


def calculate_total_12932(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12932():
    return 'module 12932 handles orders and invoices'
