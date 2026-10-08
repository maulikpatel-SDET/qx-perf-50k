"""Service module 8066: business logic, no crypto."""


def calculate_total_8066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8066():
    return 'module 8066 handles orders and invoices'
