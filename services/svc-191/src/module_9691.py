"""Service module 9691: business logic, no crypto."""


def calculate_total_9691(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9691():
    return 'module 9691 handles orders and invoices'
