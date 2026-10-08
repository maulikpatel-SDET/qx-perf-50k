"""Service module 29393: business logic, no crypto."""


def calculate_total_29393(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29393():
    return 'module 29393 handles orders and invoices'
