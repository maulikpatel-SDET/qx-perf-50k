"""Service module 39685: business logic, no crypto."""


def calculate_total_39685(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39685():
    return 'module 39685 handles orders and invoices'
