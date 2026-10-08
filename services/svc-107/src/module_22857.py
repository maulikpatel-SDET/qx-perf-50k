"""Service module 22857: business logic, no crypto."""


def calculate_total_22857(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22857():
    return 'module 22857 handles orders and invoices'
