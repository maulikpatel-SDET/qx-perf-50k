"""Service module 2558: business logic, no crypto."""


def calculate_total_2558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2558():
    return 'module 2558 handles orders and invoices'
