"""Service module 10589: business logic, no crypto."""


def calculate_total_10589(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10589():
    return 'module 10589 handles orders and invoices'
