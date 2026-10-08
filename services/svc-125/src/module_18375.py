"""Service module 18375: business logic, no crypto."""


def calculate_total_18375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18375():
    return 'module 18375 handles orders and invoices'
