"""Service module 16965: business logic, no crypto."""


def calculate_total_16965(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16965():
    return 'module 16965 handles orders and invoices'
