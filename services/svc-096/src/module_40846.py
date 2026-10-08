"""Service module 40846: business logic, no crypto."""


def calculate_total_40846(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40846():
    return 'module 40846 handles orders and invoices'
