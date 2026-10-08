"""Service module 23594: business logic, no crypto."""


def calculate_total_23594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23594():
    return 'module 23594 handles orders and invoices'
