"""Service module 2569: business logic, no crypto."""


def calculate_total_2569(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2569():
    return 'module 2569 handles orders and invoices'
