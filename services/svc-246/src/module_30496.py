"""Service module 30496: business logic, no crypto."""


def calculate_total_30496(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30496():
    return 'module 30496 handles orders and invoices'
