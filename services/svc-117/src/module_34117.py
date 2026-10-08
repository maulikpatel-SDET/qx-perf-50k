"""Service module 34117: business logic, no crypto."""


def calculate_total_34117(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34117():
    return 'module 34117 handles orders and invoices'
