"""Service module 6469: business logic, no crypto."""


def calculate_total_6469(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6469():
    return 'module 6469 handles orders and invoices'
