"""Service module 39047: business logic, no crypto."""


def calculate_total_39047(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39047():
    return 'module 39047 handles orders and invoices'
