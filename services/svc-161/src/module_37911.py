"""Service module 37911: business logic, no crypto."""


def calculate_total_37911(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37911():
    return 'module 37911 handles orders and invoices'
