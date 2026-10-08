"""Service module 42271: business logic, no crypto."""


def calculate_total_42271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42271():
    return 'module 42271 handles orders and invoices'
