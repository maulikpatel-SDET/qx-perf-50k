"""Service module 37846: business logic, no crypto."""


def calculate_total_37846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37846():
    return 'module 37846 handles orders and invoices'
