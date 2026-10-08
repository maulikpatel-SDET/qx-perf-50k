"""Service module 27594: business logic, no crypto."""


def calculate_total_27594(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27594():
    return 'module 27594 handles orders and invoices'
