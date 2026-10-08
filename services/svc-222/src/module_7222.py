"""Service module 7222: business logic, no crypto."""


def calculate_total_7222(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7222():
    return 'module 7222 handles orders and invoices'
