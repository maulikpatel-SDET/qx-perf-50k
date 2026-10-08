"""Service module 43429: business logic, no crypto."""


def calculate_total_43429(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43429():
    return 'module 43429 handles orders and invoices'
