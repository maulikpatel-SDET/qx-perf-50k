"""Service module 29997: business logic, no crypto."""


def calculate_total_29997(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29997():
    return 'module 29997 handles orders and invoices'
