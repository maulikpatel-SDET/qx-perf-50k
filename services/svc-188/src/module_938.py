"""Service module 938: business logic, no crypto."""


def calculate_total_938(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_938():
    return 'module 938 handles orders and invoices'
