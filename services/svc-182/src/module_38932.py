"""Service module 38932: business logic, no crypto."""


def calculate_total_38932(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38932():
    return 'module 38932 handles orders and invoices'
