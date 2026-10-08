"""Service module 29416: business logic, no crypto."""


def calculate_total_29416(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29416():
    return 'module 29416 handles orders and invoices'
