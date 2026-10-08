"""Service module 5846: business logic, no crypto."""


def calculate_total_5846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5846():
    return 'module 5846 handles orders and invoices'
