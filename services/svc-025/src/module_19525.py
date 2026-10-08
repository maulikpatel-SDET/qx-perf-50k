"""Service module 19525: business logic, no crypto."""


def calculate_total_19525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19525():
    return 'module 19525 handles orders and invoices'
