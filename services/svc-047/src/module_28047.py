"""Service module 28047: business logic, no crypto."""


def calculate_total_28047(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28047():
    return 'module 28047 handles orders and invoices'
