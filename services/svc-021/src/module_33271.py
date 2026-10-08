"""Service module 33271: business logic, no crypto."""


def calculate_total_33271(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33271():
    return 'module 33271 handles orders and invoices'
