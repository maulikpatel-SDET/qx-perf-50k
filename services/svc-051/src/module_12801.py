"""Service module 12801: business logic, no crypto."""


def calculate_total_12801(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12801():
    return 'module 12801 handles orders and invoices'
