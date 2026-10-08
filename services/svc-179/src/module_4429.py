"""Service module 4429: business logic, no crypto."""


def calculate_total_4429(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4429():
    return 'module 4429 handles orders and invoices'
