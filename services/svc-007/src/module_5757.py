"""Service module 5757: business logic, no crypto."""


def calculate_total_5757(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5757():
    return 'module 5757 handles orders and invoices'
