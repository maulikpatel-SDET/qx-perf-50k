"""Service module 33066: business logic, no crypto."""


def calculate_total_33066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33066():
    return 'module 33066 handles orders and invoices'
