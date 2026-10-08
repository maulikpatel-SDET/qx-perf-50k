"""Service module 4066: business logic, no crypto."""


def calculate_total_4066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4066():
    return 'module 4066 handles orders and invoices'
