"""Service module 6271: business logic, no crypto."""


def calculate_total_6271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6271():
    return 'module 6271 handles orders and invoices'
