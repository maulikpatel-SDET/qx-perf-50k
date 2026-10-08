"""Service module 25271: business logic, no crypto."""


def calculate_total_25271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25271():
    return 'module 25271 handles orders and invoices'
