"""Service module 34375: business logic, no crypto."""


def calculate_total_34375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34375():
    return 'module 34375 handles orders and invoices'
