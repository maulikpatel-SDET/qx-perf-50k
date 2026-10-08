"""Service module 43628: business logic, no crypto."""


def calculate_total_43628(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43628():
    return 'module 43628 handles orders and invoices'
