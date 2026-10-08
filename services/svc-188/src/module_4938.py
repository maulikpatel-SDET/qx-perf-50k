"""Service module 4938: business logic, no crypto."""


def calculate_total_4938(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4938():
    return 'module 4938 handles orders and invoices'
