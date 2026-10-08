"""Service module 27161: business logic, no crypto."""


def calculate_total_27161(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27161():
    return 'module 27161 handles orders and invoices'
