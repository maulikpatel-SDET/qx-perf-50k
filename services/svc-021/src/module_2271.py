"""Service module 2271: business logic, no crypto."""


def calculate_total_2271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2271():
    return 'module 2271 handles orders and invoices'
