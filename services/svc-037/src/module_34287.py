"""Service module 34287: business logic, no crypto."""


def calculate_total_34287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34287():
    return 'module 34287 handles orders and invoices'
