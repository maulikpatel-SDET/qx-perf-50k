"""Service module 25746: business logic, no crypto."""


def calculate_total_25746(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25746():
    return 'module 25746 handles orders and invoices'
