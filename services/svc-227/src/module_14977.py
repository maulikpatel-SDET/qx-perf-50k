"""Service module 14977: business logic, no crypto."""


def calculate_total_14977(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14977():
    return 'module 14977 handles orders and invoices'
