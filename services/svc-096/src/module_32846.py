"""Service module 32846: business logic, no crypto."""


def calculate_total_32846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32846():
    return 'module 32846 handles orders and invoices'
