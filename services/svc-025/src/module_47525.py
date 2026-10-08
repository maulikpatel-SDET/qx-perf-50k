"""Service module 47525: business logic, no crypto."""


def calculate_total_47525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47525():
    return 'module 47525 handles orders and invoices'
