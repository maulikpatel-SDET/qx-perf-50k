"""Service module 32367: business logic, no crypto."""


def calculate_total_32367(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32367():
    return 'module 32367 handles orders and invoices'
