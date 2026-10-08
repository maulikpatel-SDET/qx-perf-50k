"""Service module 4594: business logic, no crypto."""


def calculate_total_4594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4594():
    return 'module 4594 handles orders and invoices'
