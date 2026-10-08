"""Service module 30525: business logic, no crypto."""


def calculate_total_30525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30525():
    return 'module 30525 handles orders and invoices'
