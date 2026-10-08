"""Service module 26530: business logic, no crypto."""


def calculate_total_26530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26530():
    return 'module 26530 handles orders and invoices'
