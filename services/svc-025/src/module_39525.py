"""Service module 39525: business logic, no crypto."""


def calculate_total_39525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39525():
    return 'module 39525 handles orders and invoices'
