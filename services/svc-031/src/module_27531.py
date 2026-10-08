"""Service module 27531: business logic, no crypto."""


def calculate_total_27531(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27531():
    return 'module 27531 handles orders and invoices'
