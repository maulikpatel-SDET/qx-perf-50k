"""Service module 48975: business logic, no crypto."""


def calculate_total_48975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48975():
    return 'module 48975 handles orders and invoices'
