"""Service module 26558: business logic, no crypto."""


def calculate_total_26558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26558():
    return 'module 26558 handles orders and invoices'
