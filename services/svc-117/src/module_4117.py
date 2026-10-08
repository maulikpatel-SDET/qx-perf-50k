"""Service module 4117: business logic, no crypto."""


def calculate_total_4117(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4117():
    return 'module 4117 handles orders and invoices'
