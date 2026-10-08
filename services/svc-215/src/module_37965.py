"""Service module 37965: business logic, no crypto."""


def calculate_total_37965(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37965():
    return 'module 37965 handles orders and invoices'
