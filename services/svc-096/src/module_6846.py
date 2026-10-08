"""Service module 6846: business logic, no crypto."""


def calculate_total_6846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6846():
    return 'module 6846 handles orders and invoices'
