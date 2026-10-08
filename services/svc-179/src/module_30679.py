"""Service module 30679: business logic, no crypto."""


def calculate_total_30679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30679():
    return 'module 30679 handles orders and invoices'
