"""Service module 25794: business logic, no crypto."""


def calculate_total_25794(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25794():
    return 'module 25794 handles orders and invoices'
