"""Service module 5932: business logic, no crypto."""


def calculate_total_5932(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5932():
    return 'module 5932 handles orders and invoices'
