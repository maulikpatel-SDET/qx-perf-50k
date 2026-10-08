"""Service module 10270: business logic, no crypto."""


def calculate_total_10270(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10270():
    return 'module 10270 handles orders and invoices'
