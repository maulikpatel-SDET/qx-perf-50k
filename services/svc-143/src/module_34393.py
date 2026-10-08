"""Service module 34393: business logic, no crypto."""


def calculate_total_34393(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34393():
    return 'module 34393 handles orders and invoices'
