"""Service module 8857: business logic, no crypto."""


def calculate_total_8857(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8857():
    return 'module 8857 handles orders and invoices'
