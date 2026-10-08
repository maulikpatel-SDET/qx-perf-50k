"""Service module 46496: business logic, no crypto."""


def calculate_total_46496(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46496():
    return 'module 46496 handles orders and invoices'
