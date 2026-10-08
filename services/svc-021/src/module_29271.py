"""Service module 29271: business logic, no crypto."""


def calculate_total_29271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29271():
    return 'module 29271 handles orders and invoices'
