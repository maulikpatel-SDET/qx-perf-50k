"""Service module 39558: business logic, no crypto."""


def calculate_total_39558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39558():
    return 'module 39558 handles orders and invoices'
