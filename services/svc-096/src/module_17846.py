"""Service module 17846: business logic, no crypto."""


def calculate_total_17846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17846():
    return 'module 17846 handles orders and invoices'
