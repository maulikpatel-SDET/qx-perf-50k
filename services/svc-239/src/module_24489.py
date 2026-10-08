"""Service module 24489: business logic, no crypto."""


def calculate_total_24489(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24489():
    return 'module 24489 handles orders and invoices'
