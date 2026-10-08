"""Service module 38210: business logic, no crypto."""


def calculate_total_38210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38210():
    return 'module 38210 handles orders and invoices'
