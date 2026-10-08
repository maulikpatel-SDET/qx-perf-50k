"""Service module 40604: business logic, no crypto."""


def calculate_total_40604(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40604():
    return 'module 40604 handles orders and invoices'
