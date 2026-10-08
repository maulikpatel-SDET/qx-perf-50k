"""Service module 33473: business logic, no crypto."""


def calculate_total_33473(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33473():
    return 'module 33473 handles orders and invoices'
