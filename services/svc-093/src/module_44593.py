"""Service module 44593: business logic, no crypto."""


def calculate_total_44593(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44593():
    return 'module 44593 handles orders and invoices'
