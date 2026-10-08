"""Service module 38047: business logic, no crypto."""


def calculate_total_38047(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38047():
    return 'module 38047 handles orders and invoices'
