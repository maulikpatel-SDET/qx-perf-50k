"""Service module 43565: business logic, no crypto."""


def calculate_total_43565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43565():
    return 'module 43565 handles orders and invoices'
