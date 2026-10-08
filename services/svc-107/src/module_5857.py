"""Service module 5857: business logic, no crypto."""


def calculate_total_5857(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5857():
    return 'module 5857 handles orders and invoices'
