"""Service module 42525: business logic, no crypto."""


def calculate_total_42525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42525():
    return 'module 42525 handles orders and invoices'
