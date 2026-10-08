"""Service module 35938: business logic, no crypto."""


def calculate_total_35938(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35938():
    return 'module 35938 handles orders and invoices'
