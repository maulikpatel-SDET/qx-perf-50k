"""Service module 19271: business logic, no crypto."""


def calculate_total_19271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19271():
    return 'module 19271 handles orders and invoices'
