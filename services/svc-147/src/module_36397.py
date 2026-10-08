"""Service module 36397: business logic, no crypto."""


def calculate_total_36397(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36397():
    return 'module 36397 handles orders and invoices'
