"""Service module 39965: business logic, no crypto."""


def calculate_total_39965(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39965():
    return 'module 39965 handles orders and invoices'
