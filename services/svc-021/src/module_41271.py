"""Service module 41271: business logic, no crypto."""


def calculate_total_41271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41271():
    return 'module 41271 handles orders and invoices'
