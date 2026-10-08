"""Service module 29469: business logic, no crypto."""


def calculate_total_29469(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29469():
    return 'module 29469 handles orders and invoices'
