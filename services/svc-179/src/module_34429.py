"""Service module 34429: business logic, no crypto."""


def calculate_total_34429(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34429():
    return 'module 34429 handles orders and invoices'
