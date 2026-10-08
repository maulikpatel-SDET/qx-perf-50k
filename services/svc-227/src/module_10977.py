"""Service module 10977: business logic, no crypto."""


def calculate_total_10977(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10977():
    return 'module 10977 handles orders and invoices'
