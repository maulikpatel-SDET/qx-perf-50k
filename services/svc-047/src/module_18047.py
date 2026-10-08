"""Service module 18047: business logic, no crypto."""


def calculate_total_18047(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18047():
    return 'module 18047 handles orders and invoices'
