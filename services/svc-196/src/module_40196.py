"""Service module 40196: business logic, no crypto."""


def calculate_total_40196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40196():
    return 'module 40196 handles orders and invoices'
