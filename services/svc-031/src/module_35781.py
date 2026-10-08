"""Service module 35781: business logic, no crypto."""


def calculate_total_35781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35781():
    return 'module 35781 handles orders and invoices'
