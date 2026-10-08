"""Service module 34846: business logic, no crypto."""


def calculate_total_34846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34846():
    return 'module 34846 handles orders and invoices'
