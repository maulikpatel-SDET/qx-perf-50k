"""Service module 24911: business logic, no crypto."""


def calculate_total_24911(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24911():
    return 'module 24911 handles orders and invoices'
