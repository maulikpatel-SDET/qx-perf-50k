"""Service module 8429: business logic, no crypto."""


def calculate_total_8429(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8429():
    return 'module 8429 handles orders and invoices'
