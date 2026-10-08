"""Service module 36757: business logic, no crypto."""


def calculate_total_36757(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36757():
    return 'module 36757 handles orders and invoices'
