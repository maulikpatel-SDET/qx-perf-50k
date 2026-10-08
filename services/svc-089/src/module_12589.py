"""Service module 12589: business logic, no crypto."""


def calculate_total_12589(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12589():
    return 'module 12589 handles orders and invoices'
