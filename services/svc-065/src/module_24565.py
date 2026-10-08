"""Service module 24565: business logic, no crypto."""


def calculate_total_24565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24565():
    return 'module 24565 handles orders and invoices'
