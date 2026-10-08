"""Service module 24594: business logic, no crypto."""


def calculate_total_24594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24594():
    return 'module 24594 handles orders and invoices'
