"""Service module 46161: business logic, no crypto."""


def calculate_total_46161(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46161():
    return 'module 46161 handles orders and invoices'
