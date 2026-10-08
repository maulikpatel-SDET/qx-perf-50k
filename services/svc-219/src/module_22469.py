"""Service module 22469: business logic, no crypto."""


def calculate_total_22469(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22469():
    return 'module 22469 handles orders and invoices'
