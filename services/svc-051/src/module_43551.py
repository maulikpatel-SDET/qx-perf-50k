"""Service module 43551: business logic, no crypto."""


def calculate_total_43551(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43551():
    return 'module 43551 handles orders and invoices'
