"""Service module 12965: business logic, no crypto."""


def calculate_total_12965(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12965():
    return 'module 12965 handles orders and invoices'
