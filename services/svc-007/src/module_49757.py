"""Service module 49757: business logic, no crypto."""


def calculate_total_49757(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49757():
    return 'module 49757 handles orders and invoices'
