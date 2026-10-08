"""Service module 12791: business logic, no crypto."""


def calculate_total_12791(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12791():
    return 'module 12791 handles orders and invoices'
