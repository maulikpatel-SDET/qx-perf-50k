"""Service module 1066: business logic, no crypto."""


def calculate_total_1066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1066():
    return 'module 1066 handles orders and invoices'
