"""Service module 13566: business logic, no crypto."""


def calculate_total_13566(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13566():
    return 'module 13566 handles orders and invoices'
