"""Service module 40977: business logic, no crypto."""


def calculate_total_40977(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40977():
    return 'module 40977 handles orders and invoices'
