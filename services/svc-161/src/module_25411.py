"""Service module 25411: business logic, no crypto."""


def calculate_total_25411(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25411():
    return 'module 25411 handles orders and invoices'
