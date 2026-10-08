"""Service module 46566: business logic, no crypto."""


def calculate_total_46566(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46566():
    return 'module 46566 handles orders and invoices'
