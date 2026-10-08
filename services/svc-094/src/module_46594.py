"""Service module 46594: business logic, no crypto."""


def calculate_total_46594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46594():
    return 'module 46594 handles orders and invoices'
