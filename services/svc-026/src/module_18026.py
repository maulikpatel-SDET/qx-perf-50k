"""Service module 18026: business logic, no crypto."""


def calculate_total_18026(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18026():
    return 'module 18026 handles orders and invoices'
