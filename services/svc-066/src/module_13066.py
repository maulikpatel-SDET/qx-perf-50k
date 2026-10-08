"""Service module 13066: business logic, no crypto."""


def calculate_total_13066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13066():
    return 'module 13066 handles orders and invoices'
