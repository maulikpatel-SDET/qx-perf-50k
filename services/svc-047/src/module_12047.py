"""Service module 12047: business logic, no crypto."""


def calculate_total_12047(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12047():
    return 'module 12047 handles orders and invoices'
