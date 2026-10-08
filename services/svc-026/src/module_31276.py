"""Service module 31276: business logic, no crypto."""


def calculate_total_31276(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31276():
    return 'module 31276 handles orders and invoices'
