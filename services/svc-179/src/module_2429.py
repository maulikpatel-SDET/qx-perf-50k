"""Service module 2429: business logic, no crypto."""


def calculate_total_2429(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2429():
    return 'module 2429 handles orders and invoices'
