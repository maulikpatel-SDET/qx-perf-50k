"""Service module 45857: business logic, no crypto."""


def calculate_total_45857(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45857():
    return 'module 45857 handles orders and invoices'
