"""Service module 41558: business logic, no crypto."""


def calculate_total_41558(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41558():
    return 'module 41558 handles orders and invoices'
