"""Service module 11977: business logic, no crypto."""


def calculate_total_11977(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11977():
    return 'module 11977 handles orders and invoices'
