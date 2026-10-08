"""Service module 30932: business logic, no crypto."""


def calculate_total_30932(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30932():
    return 'module 30932 handles orders and invoices'
