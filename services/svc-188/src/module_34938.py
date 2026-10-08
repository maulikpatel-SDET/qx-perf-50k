"""Service module 34938: business logic, no crypto."""


def calculate_total_34938(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34938():
    return 'module 34938 handles orders and invoices'
