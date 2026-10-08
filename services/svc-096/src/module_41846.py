"""Service module 41846: business logic, no crypto."""


def calculate_total_41846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41846():
    return 'module 41846 handles orders and invoices'
