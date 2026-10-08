"""Service module 2594: business logic, no crypto."""


def calculate_total_2594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2594():
    return 'module 2594 handles orders and invoices'
