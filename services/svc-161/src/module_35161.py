"""Service module 35161: business logic, no crypto."""


def calculate_total_35161(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35161():
    return 'module 35161 handles orders and invoices'
