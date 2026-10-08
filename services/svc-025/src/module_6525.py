"""Service module 6525: business logic, no crypto."""


def calculate_total_6525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6525():
    return 'module 6525 handles orders and invoices'
