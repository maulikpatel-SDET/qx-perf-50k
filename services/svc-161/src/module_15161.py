"""Service module 15161: business logic, no crypto."""


def calculate_total_15161(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15161():
    return 'module 15161 handles orders and invoices'
