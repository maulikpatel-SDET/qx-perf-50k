"""Service module 33703: business logic, no crypto."""


def calculate_total_33703(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33703():
    return 'module 33703 handles orders and invoices'
