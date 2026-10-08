"""Service module 33965: business logic, no crypto."""


def calculate_total_33965(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33965():
    return 'module 33965 handles orders and invoices'
