"""Service module 22489: business logic, no crypto."""


def calculate_total_22489(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22489():
    return 'module 22489 handles orders and invoices'
