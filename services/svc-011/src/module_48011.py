"""Service module 48011: business logic, no crypto."""


def calculate_total_48011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48011():
    return 'module 48011 handles orders and invoices'
