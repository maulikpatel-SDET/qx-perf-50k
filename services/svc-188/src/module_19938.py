"""Service module 19938: business logic, no crypto."""


def calculate_total_19938(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19938():
    return 'module 19938 handles orders and invoices'
