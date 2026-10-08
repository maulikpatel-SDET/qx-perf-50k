"""Service module 2496: business logic, no crypto."""


def calculate_total_2496(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2496():
    return 'module 2496 handles orders and invoices'
