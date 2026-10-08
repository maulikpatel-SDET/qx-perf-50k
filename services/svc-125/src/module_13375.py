"""Service module 13375: business logic, no crypto."""


def calculate_total_13375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13375():
    return 'module 13375 handles orders and invoices'
