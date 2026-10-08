"""Service module 5593: business logic, no crypto."""


def calculate_total_5593(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5593():
    return 'module 5593 handles orders and invoices'
