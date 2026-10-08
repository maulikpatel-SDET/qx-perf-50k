"""Service module 26469: business logic, no crypto."""


def calculate_total_26469(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26469():
    return 'module 26469 handles orders and invoices'
