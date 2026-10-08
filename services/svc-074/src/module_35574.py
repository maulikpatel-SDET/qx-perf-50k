"""Service module 35574: business logic, no crypto."""


def calculate_total_35574(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35574():
    return 'module 35574 handles orders and invoices'
