"""Service module 21474: business logic, no crypto."""


def calculate_total_21474(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21474():
    return 'module 21474 handles orders and invoices'
