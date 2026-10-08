"""Service module 17271: business logic, no crypto."""


def calculate_total_17271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17271():
    return 'module 17271 handles orders and invoices'
