"""Service module 33531: business logic, no crypto."""


def calculate_total_33531(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33531():
    return 'module 33531 handles orders and invoices'
