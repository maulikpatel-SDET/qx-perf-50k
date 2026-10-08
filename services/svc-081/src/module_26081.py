"""Service module 26081: business logic, no crypto."""


def calculate_total_26081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26081():
    return 'module 26081 handles orders and invoices'
