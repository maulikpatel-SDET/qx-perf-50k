"""Service module 6047: business logic, no crypto."""


def calculate_total_6047(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6047():
    return 'module 6047 handles orders and invoices'
