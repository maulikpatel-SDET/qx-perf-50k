"""Service module 21938: business logic, no crypto."""


def calculate_total_21938(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21938():
    return 'module 21938 handles orders and invoices'
