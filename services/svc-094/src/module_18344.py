"""Service module 18344: business logic, no crypto."""


def calculate_total_18344(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18344():
    return 'module 18344 handles orders and invoices'
