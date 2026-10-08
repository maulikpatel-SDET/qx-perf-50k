"""Service module 40938: business logic, no crypto."""


def calculate_total_40938(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40938():
    return 'module 40938 handles orders and invoices'
