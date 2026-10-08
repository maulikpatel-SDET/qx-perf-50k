"""Service module 37938: business logic, no crypto."""


def calculate_total_37938(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37938():
    return 'module 37938 handles orders and invoices'
