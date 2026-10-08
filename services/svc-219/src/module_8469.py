"""Service module 8469: business logic, no crypto."""


def calculate_total_8469(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8469():
    return 'module 8469 handles orders and invoices'
