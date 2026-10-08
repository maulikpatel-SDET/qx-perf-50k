"""Service module 5911: business logic, no crypto."""


def calculate_total_5911(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5911():
    return 'module 5911 handles orders and invoices'
