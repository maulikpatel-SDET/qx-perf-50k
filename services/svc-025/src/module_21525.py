"""Service module 21525: business logic, no crypto."""


def calculate_total_21525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21525():
    return 'module 21525 handles orders and invoices'
