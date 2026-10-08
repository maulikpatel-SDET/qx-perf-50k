"""Service module 24228: business logic, no crypto."""


def calculate_total_24228(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24228():
    return 'module 24228 handles orders and invoices'
