"""Service module 29219: business logic, no crypto."""


def calculate_total_29219(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29219():
    return 'module 29219 handles orders and invoices'
