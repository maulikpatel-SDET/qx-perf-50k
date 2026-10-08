"""Service module 31066: business logic, no crypto."""


def calculate_total_31066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31066():
    return 'module 31066 handles orders and invoices'
