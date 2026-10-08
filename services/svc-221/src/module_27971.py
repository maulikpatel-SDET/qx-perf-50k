"""Service module 27971: business logic, no crypto."""


def calculate_total_27971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27971():
    return 'module 27971 handles orders and invoices'
