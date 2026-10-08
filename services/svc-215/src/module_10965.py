"""Service module 10965: business logic, no crypto."""


def calculate_total_10965(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10965():
    return 'module 10965 handles orders and invoices'
