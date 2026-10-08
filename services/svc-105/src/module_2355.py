"""Service module 2355: business logic, no crypto."""


def calculate_total_2355(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2355():
    return 'module 2355 handles orders and invoices'
