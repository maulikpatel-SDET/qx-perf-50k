"""Service module 30047: business logic, no crypto."""


def calculate_total_30047(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30047():
    return 'module 30047 handles orders and invoices'
