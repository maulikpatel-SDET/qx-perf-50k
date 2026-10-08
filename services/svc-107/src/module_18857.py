"""Service module 18857: business logic, no crypto."""


def calculate_total_18857(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18857():
    return 'module 18857 handles orders and invoices'
