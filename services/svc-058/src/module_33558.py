"""Service module 33558: business logic, no crypto."""


def calculate_total_33558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33558():
    return 'module 33558 handles orders and invoices'
