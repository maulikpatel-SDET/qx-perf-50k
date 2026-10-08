"""Service module 35792: business logic, no crypto."""


def calculate_total_35792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35792():
    return 'module 35792 handles orders and invoices'
