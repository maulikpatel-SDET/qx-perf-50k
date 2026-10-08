"""Service module 6594: business logic, no crypto."""


def calculate_total_6594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6594():
    return 'module 6594 handles orders and invoices'
