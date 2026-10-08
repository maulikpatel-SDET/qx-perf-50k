"""Service module 30977: business logic, no crypto."""


def calculate_total_30977(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30977():
    return 'module 30977 handles orders and invoices'
