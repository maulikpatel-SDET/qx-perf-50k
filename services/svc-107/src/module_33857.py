"""Service module 33857: business logic, no crypto."""


def calculate_total_33857(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33857():
    return 'module 33857 handles orders and invoices'
