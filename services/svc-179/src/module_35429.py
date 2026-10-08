"""Service module 35429: business logic, no crypto."""


def calculate_total_35429(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35429():
    return 'module 35429 handles orders and invoices'
