"""Service module 6569: business logic, no crypto."""


def calculate_total_6569(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6569():
    return 'module 6569 handles orders and invoices'
