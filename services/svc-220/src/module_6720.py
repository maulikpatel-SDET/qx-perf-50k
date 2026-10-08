"""Service module 6720: business logic, no crypto."""


def calculate_total_6720(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6720():
    return 'module 6720 handles orders and invoices'
