"""Service module 31496: business logic, no crypto."""


def calculate_total_31496(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31496():
    return 'module 31496 handles orders and invoices'
