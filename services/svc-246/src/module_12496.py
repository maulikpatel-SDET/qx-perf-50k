"""Service module 12496: business logic, no crypto."""


def calculate_total_12496(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12496():
    return 'module 12496 handles orders and invoices'
